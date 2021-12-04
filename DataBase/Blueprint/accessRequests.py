from app import app
from DataBase.schemas import AccessSchema
from DataBase.models import Access, User
from flask import request, jsonify
from datetime import datetime, timedelta
from flask_httpauth import HTTPBasicAuth
import bcrypt
from DataBase.models import Session

session = Session()

from DataBase.db_utils import (
    InvalidUsage,
    create_entry,
    get_entries,
    get_entry_by_id,
    delete_entity,
    check_time
)

auth = HTTPBasicAuth()

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
        rv['status_code'] = self.status_code
        return rv

@auth.verify_password
def verify_password(username, password):
    user = session.query(User).filter_by(username=username).first()
    print(user)
    if not user:
        return False
    print(bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")))
    if not bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
        return False
    if user:
        return user

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.route("/access", methods=["POST"])  # create new access
@auth.login_required
def create_access():
    cur_user = auth.current_user()
    print(cur_user)
    access_data = AccessSchema().load(request.get_json())
    user_id = request.json.get('user_id', None)
    print(user_id)
    if int(cur_user.id) == int(user_id):
        start = request.json.get('start', None)
        start = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
        end = request.json.get('end', None)
        end = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
        time = end - start
        if time < timedelta(hours=1):
            raise InvalidUsage("Invalid access time (too short)", status_code=400)
        if time > timedelta(hours=5):
            raise InvalidUsage("Invalid access time (too long)", status_code=400)

        auditorium_id = int(request.json.get('auditorium_id', None))
        check_time(Access, AccessSchema, auditorium_id, start, end)
        return create_entry(Access, AccessSchema, **access_data)
    else:
        raise InvalidUsage("Invalid user Id", status_code=404)


# curl -X POST -u Pax1:abcdefg -H "Content-Type:application/json" --data-binary "{\"auditorium_id\": \"1\", \"user_id\": \"1\", \"start\": \"2021-01-01 1:00:00\", \"end\": \"2021-01-01 3:00:00\"}" http://localhost:5000/access

@app.route("/access", methods=["GET"])  # get all accesses
@auth.login_required
def get_access():
    cur_user = auth.current_user()
    print(cur_user)
    return jsonify(AccessSchema(many=True).dump(session.query(Access).filter_by(user_id=cur_user.id).all()))

# curl -X GET -u Pax1:abcdefg http://localhost:5000/access

@app.route("/access/<int:access_id>", methods=["GET"])  # get access by id
@auth.login_required
def get_access_by_id(access_id):
    cur_user = auth.current_user()
    print(cur_user)
    temp = session.query(Access).filter_by(id = access_id).first()
    print(temp.user_id, temp.auditorium_id)
    if int(cur_user.id) == int(temp.user_id):
        print("done")
        return get_entry_by_id(Access, AccessSchema, int(access_id))
    else:
        raise InvalidUsage("Invalid user Id", status_code=404)


# curl -X GET -u Pax2:abcdefg http://localhost:5000/access/1

@app.route("/access/<int:access_id>", methods=["DELETE"])  # delete access by id
@auth.login_required
def delete_access_by_id(access_id):
    cur_user = auth.current_user()
    temp = session.query(Access).filter_by(id=int(access_id)).first()
    print(temp)
    if temp is None:
        raise InvalidUsage("Invalid access Id", status_code=404)
    print(cur_user)

    if int(cur_user.id) == int(temp.user_id):
        return delete_entity(Access, AccessSchema, int(access_id))
    else:
        raise InvalidUsage("Invalid user Id", status_code=404)

# curl -X DELETE -u Pax2:abcdefg http://localhost:5000/access/1