from app import app

from DataBase.schemas import (
    AccessSchema)

from DataBase.db_utils import (
    create_entry,
    get_entry_by_id,
    update_entry_by_id,
    delete_entry_by_id,
)

from DataBase.models import Access

from flask import request, jsonify


@app.route("/access", methods=["POST"])  # create new access
def create_access():
    access_data = AccessSchema().load(request.get_json())
    access_obj = create_entry(Access, **access_data)
    return jsonify(AccessSchema().dump(access_obj))


@app.route("/access", methods=["GET"])  # get all accesses
def get_access():
    access_array = Access.query.all()
    return jsonify(AccessSchema(many=True).dump(access_array))
#
#
# @app.route("/access/<int:id>,<int:id>", methods=["GET"])  # get access by id
# def get_access_by_id(id):
#     access_obj = get_entry_by_id(Access, id)
#     return jsonify(AccessSchema().dump(access_obj))
#
#
# @app.route("/access/<int:id>", methods=["DELETE"])  # delete access by id
# def delete_access_by_id(id):
#     access_obj = delete_entry_by_id(Access, id)
#     return jsonify(AccessSchema().dump(access_obj))
