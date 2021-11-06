from app import app

from DataBase.schemas import (
    AuditoriumSchema)

from DataBase.db_utils import (
    create_entry,
    get_entry_by_id,
    update_entry_by_id,
    delete_entry_by_id,
)

from DataBase.models import Auditorium

from flask import request, jsonify


@app.route("/auditorium", methods=["POST"])  # create new auditorium
def create_auditorium():
    auditorium_data = AuditoriumSchema().load(request.get_json())
    auditorium_obj = create_entry(Auditorium, **auditorium_data)
    return jsonify(AuditoriumSchema().dump(auditorium_obj))


@app.route("/auditorium", methods=["GET"])  # get all auditoriums
def get_auditorium():
    auditorium_array = Auditorium.query.all()
    return jsonify(AuditoriumSchema(many=True).dump(auditorium_array))


@app.route("/auditorium/<int:id>", methods=["GET"])  # get auditorium by id
def get_auditorium_by_id(id):
    auditorium_obj = get_entry_by_id(Auditorium, id)
    return jsonify(AuditoriumSchema().dump(auditorium_obj))


@app.route("/auditorium/<int:id>", methods=["PUT"])  # update auditorium by id
def update_auditorium_by_id(id):
    auditorium_data = AuditoriumSchema().load(request.get_json())
    auditorium_obj = update_entry_by_id(Auditorium, id, **auditorium_data)
    return jsonify(AuditoriumSchema().dump(auditorium_obj))


@app.route("/auditorium/<int:id>", methods=["DELETE"])  # delete auditorium by id
def delete_auditorium_by_id(id):
    auditorium_obj = delete_entry_by_id(Auditorium, id)
    return jsonify(AuditoriumSchema().dump(auditorium_obj))
