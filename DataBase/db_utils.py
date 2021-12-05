from DataBase.debug_enable import app
from DataBase.models import Session
from flask import jsonify, request
from functools import wraps

import sqlalchemy
from datetime import datetime, timedelta
import json

session = Session()


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


def db_lifecycle(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if isinstance(e, ValueError):
                return jsonify({'message': e.args[0], 'type': 'ValueError'}), 400
            elif isinstance(e, AttributeError):
                return jsonify({'message': e.args[0], 'type': 'AttributeError'}), 400
            elif isinstance(e, KeyError):
                return jsonify({'message': e.args[0], 'type': 'KeyError'}), 400
            elif isinstance(e, TypeError):
                return jsonify({'message': e.args[0], 'type': 'TypeError'}), 400
            elif isinstance(e, sqlalchemy.exc.IntegrityError):
                if str(e.args[0]).find("Duplicate entry") != -1:
                    raise InvalidUsage("Duplicate entry", status_code=400)
                if str(e.args[0]).find("Cannot delete or update a parent row: a foreign key constraint fails") != -1:
                    raise InvalidUsage("Cannot delete or update this object", status_code=400)
                if str(e.args[0]).find("Cannot add or update a child row: a foreign key constraint fails") != -1:
                    raise InvalidUsage("Cannot add or update this object, incorrect data", status_code=400)
                else:
                    raise InvalidUsage("Incorrect data", status_code=400)
            # elif isinstance(e, sqlalchemy.exc.IntegrityError):
            #     return jsonify({'message': "duplicate unique value", 'type': 'IntegrityError'}), 400
            else:
                raise e

    return wrapper


def session_lifecycle(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            rez = func(*args, **kwargs)
            session.commit()
            return rez
        except Exception as e:
            session.rollback()
            raise e

    return wrapper


@db_lifecycle
@session_lifecycle
def create_entry(model_class, model_schema, **kwargs):  # POST entity
    entry = model_class(**kwargs)
    session.add(entry)
    return jsonify(model_schema().dump(entry))


@db_lifecycle
def get_entries(model_class, model_schema):  # GET all entries
    entries = session.query(model_class).all()
    return jsonify(model_schema(many=True).dump(entries))


@db_lifecycle
def get_entry_by_id(model_class, model_schema, id):  # GET entry by id
    entry = session.query(model_class).filter_by(id=id).first()
    if entry is None:
        raise InvalidUsage("Object not found", status_code=404)
    return jsonify(model_schema().dump(entry))


@db_lifecycle
def get_entry_by_username(model_class, model_schema, username):  # GET _user_ by username
    entry = session.query(model_class).filter_by(username=username).first()
    if entry is None:
        raise InvalidUsage("Object not found", status_code=404)
    return jsonify(model_schema().dump(entry))


@db_lifecycle
@session_lifecycle
def update_entity(model_schema, entity):  # PUT entity
    data = model_schema().load(request.get_json())

    if entity is None:
        raise InvalidUsage("Object not found", status_code=404)
    for key, value in data.items():
        setattr(entity, key, value)
    return jsonify(model_schema().dump(entity))


@db_lifecycle
@session_lifecycle
def delete_entity(model_schema, entity):  # DELETE entity
    if entity is None:
        raise InvalidUsage("Object not found", status_code=404)
    session.delete(entity)
    return jsonify(model_schema().dump(entity))


@db_lifecycle
def get_entry_by_ids(model_class, model_schema, user_id, auditorium_id):  # GET access by user and auditorium ids
    entry = session.query(model_class).filter_by(user_id=user_id, auditorium_id=auditorium_id).first()
    if entry is None:
        raise InvalidUsage("Object not found", status_code=404)
    return jsonify(model_schema(many=True).dump(entry))


@db_lifecycle
@session_lifecycle
def delete_entry_by_ids(model_class, model_schema, user_id, auditorium_id):  # DELETE access by user and auditorium ids
    entry = session.query(model_class).filter_by(user_id=user_id, auditorium_id=auditorium_id).first()
    if entry is None:
        raise InvalidUsage("Object not found", status_code=404)
    session.delete(entry)
    return jsonify(model_schema().dump(entry))


@db_lifecycle
def check_time(model_class, model_schema, id, main_start, main_end):
    entries = session.query(model_class).all()
    for entry in entries:
        if entry.auditorium_id != id:
            continue
        start = entry.start
        end = entry.end
        # start = entry.json.get('start', None)
        # start = entry.strptime(start, '%Y-%m-%d %H:%M:%S')
        # end = entry.json.get('end', None)
        # end = entry.strptime(end, '%Y-%m-%d %H:%M:%S')

        if start < main_start and (end > main_start and end < main_end):
            raise InvalidUsage("Time already reserved (1)", status_code=404)

        if start > main_start and end < main_end:
            raise InvalidUsage("Time already reserved (2)", status_code=404)

        if (start > main_start and start < main_end) and end > main_end:
            raise InvalidUsage("Time already reserved (3)", status_code=404)

        if start < main_start and end > main_end:
            raise InvalidUsage("Time already reserved (4)", status_code=404)
