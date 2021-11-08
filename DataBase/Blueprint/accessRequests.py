from app import app
from DataBase.schemas import AccessSchema
from DataBase.models import Access
from flask import request

from DataBase.db_utils import (
    create_entry,
    get_entries,
    get_entry_by_ids,
    delete_entry_by_ids,
)


@app.route("/access", methods=["POST"])  # create new access
def create_access():
    access_data = AccessSchema().load(request.get_json())
    return create_entry(Access, AccessSchema, **access_data)


@app.route("/access", methods=["GET"])  # get all accesses
def get_access():
    return get_entries(Access, AccessSchema)


@app.route("/access/<int:user_id>,<int:auditorium_id>", methods=["GET"])  # get access by id
def get_access_by_two_ids(user_id, auditorium_id):
    return get_entry_by_ids(Access, AccessSchema, user_id, auditorium_id)


@app.route("/access/<int:user_id>,<int:auditorium_id>", methods=["DELETE"])  # delete access by id
def delete_access_by_two_ids(user_id, auditorium_id):
    return delete_entry_by_ids(Access, AccessSchema, user_id, auditorium_id)
