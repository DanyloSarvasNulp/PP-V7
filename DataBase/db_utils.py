from models import Session
from flask import jsonify
from functools import wraps

session = Session()


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
            else:
                return jsonify({'message': str(e), 'type': 'InternalServerError'}), 500

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
    return jsonify(model_schema().dump(entry))


@db_lifecycle
def get_entry_by_username(model_class, model_schema, username):  # GET _user_ by username
    entry = session.query(model_class).filter_by(username=username).first()
    return jsonify(model_schema().dump(entry))


@db_lifecycle
@session_lifecycle
def update_entry_by_id(model_class, model_schema, id, **kwargs):  # PUT entity by id
    entry = session.query(model_class).filter_by(id=id).first()
    for key, value in kwargs.items():
        setattr(entry, key, value)
    return jsonify(model_schema().dump(entry))


@db_lifecycle
@session_lifecycle
def delete_entry_by_id(model_class, model_schema, id):  # DELETE entity by id
    entry = session.query(model_class).filter_by(id=id).first()
    session.delete(entry)
    return jsonify(model_schema().dump(entry))


def get_entry_by_ids(model_class, user_id, auditorium_id):  # GET access by user and auditorium ids
    session = Session()
    return session.query(model_class).filter_by(user_id=user_id, auditorium_id=auditorium_id).first()


def delete_entry_by_ids(model_class, user_id, auditorium_id, commit=True):  # DELETE access by user and auditorium ids
    session = Session()
    model = session.query(model_class).filter_by(user_id=user_id, auditorium_id=auditorium_id).first()
    session.delete(model)
    if commit:
        session.commit()
    return model
