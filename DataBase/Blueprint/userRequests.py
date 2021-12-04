from DataBase.schemas import UserSchema, AccessSchema
from DataBase.models import User, Access
from flask import request, jsonify
from flask_httpauth import HTTPBasicAuth
import bcrypt
from DataBase.models import Session

session = Session()

from DataBase.db_utils import *

auth = HTTPBasicAuth()
users = {}
users["username"] = "password"


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

    if user and bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
        return user
    return False


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route("/user", methods=["POST"])  # create new user
def create_user():
    user_data = UserSchema().load(request.get_json())

    pwd = request.json.get('password', None)
    hashed_pwd = bcrypt.hashpw(pwd.encode("utf-8"), bcrypt.gensalt())
    user_data.update({"password": hashed_pwd})

    return create_entry(User, UserSchema, **user_data)


def get_entry_by_username(func):
    @wraps(func)
    def wrapper():
        entry = session.query(User).filter_by(username=auth.current_user().username).first()
        if entry is None:
            raise InvalidUsage("Object not found", status_code=404)
        return func(entry)

    return wrapper


@app.route("/user", methods=["GET"])  # get user by username
@auth.login_required
@get_entry_by_username
def get_user_by_username(entry):
    return jsonify(UserSchema().dump(entry))


@app.route("/user", methods=["PUT"])  # update user by username
@auth.login_required
@get_entry_by_username
def update_user_by_username(entry):
    return update_entity(UserSchema, entry)


@app.route("/user", methods=["DELETE"])  # delete user by username
@auth.login_required
@get_entry_by_username
def delete_user_by_username(entry):
    return delete_entity(UserSchema, entry)
