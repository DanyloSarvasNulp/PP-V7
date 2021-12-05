from app import app
from DataBase.schemas import AuditoriumSchema
from DataBase.models import Auditorium
from flask import request

from DataBase.db_utils import *


@app.route("/auditorium", methods=["POST"])  # create new auditorium
def create_auditorium():
    auditorium_data = AuditoriumSchema().load(request.get_json())
    return create_entry(Auditorium, AuditoriumSchema, **auditorium_data)


@app.route("/auditorium", methods=["GET"])  # get all auditoriums
def get_auditorium():
    return get_entries(Auditorium, AuditoriumSchema)


def get_entry_by_username(func):
    @wraps(func)
    def wrapper(num):
        entry = session.query(Auditorium).filter_by(auditorium_num=num).first()
        if entry is None:
            raise InvalidUsage("Object not found", status_code=404)  # pragma: no cover
        return func(entry)

    return wrapper


@app.route("/auditorium/<int:num>", methods=["GET"])  # get auditorium
@get_entry_by_username
def get_auditorium_by_id(entity):
    return jsonify(AuditoriumSchema().dump(entity))


@app.route("/auditorium/<int:num>", methods=["PUT"])  # update auditorium
@get_entry_by_username
def update_auditorium_by_id(entity):
    return update_entity(AuditoriumSchema, entity)


@app.route("/auditorium/<int:num>", methods=["DELETE"])  # delete auditorium
@get_entry_by_username
def delete_auditorium_by_id(entity):
    return delete_entity(AuditoriumSchema, entity)
