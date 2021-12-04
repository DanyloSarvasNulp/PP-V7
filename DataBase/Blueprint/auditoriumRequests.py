from app import app
from DataBase.schemas import AuditoriumSchema
from DataBase.models import Auditorium
from flask import request

from DataBase.db_utils import (
    create_entry,
    get_entries,
    get_entry_by_id,
    update_entity,
    delete_entity,
)
# TODO: solve problem

@app.route("/auditorium", methods=["POST"])  # create new auditorium
def create_auditorium():
    auditorium_data = AuditoriumSchema().load(request.get_json())
    return create_entry(Auditorium, AuditoriumSchema, **auditorium_data)
# curl -X POST -H "Content-Type:application/json" --data-binary "{\"max_people_count\": \"48\"}" http://localhost:5000/auditorium


@app.route("/auditorium", methods=["GET"])  # get all auditoriums
def get_auditorium():
    return get_entries(Auditorium, AuditoriumSchema)


@app.route("/auditorium/<int:id>", methods=["GET"])  # get auditorium by id
def get_auditorium_by_id(id):
    return get_entry_by_id(Auditorium, AuditoriumSchema, id)


@app.route("/auditorium/<int:id>", methods=["PUT"])  # update auditorium by id
def update_auditorium_by_id(id):
    auditorium_data = AuditoriumSchema().load(request.get_json())
    return update_entity(Auditorium, AuditoriumSchema, id, **auditorium_data)


@app.route("/auditorium/<int:id>", methods=["DELETE"])  # delete auditorium by id
def delete_auditorium_by_id(id):
    return delete_entity(Auditorium, AuditoriumSchema, id)
