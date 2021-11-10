from app import app
from DataBase.schemas import AccessSchema
from DataBase.models import Access
from flask import request
from datetime import datetime, timedelta

from DataBase.db_utils import (
    InvalidUsage,
    create_entry,
    get_entries,
    get_entry_by_ids,
    delete_entry_by_ids,
    check_time
)


@app.route("/access", methods=["POST"])  # create new access
def create_access():
    access_data = AccessSchema().load(request.get_json())

    start = request.json.get('start', None)
    start = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
    end = request.json.get('end', None)
    end = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
    time = end - start
    if time < timedelta(hours=1):
        raise InvalidUsage("Invalid access time (too short)", status_code=400)
    if time > timedelta(hours=5):
        raise InvalidUsage("Invalid access time (too long)", status_code=400)

    check_time(Access, AccessSchema, start, end)
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
