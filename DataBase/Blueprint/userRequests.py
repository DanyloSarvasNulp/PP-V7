from app import app
from DataBase.schemas import UserSchema, AccessSchema
from DataBase.models import User, Access
from flask import request, jsonify
from flask_httpauth import HTTPBasicAuth
import bcrypt
from DataBase.models import Session

session = Session()

from DataBase.db_utils import (
    create_entry,
    get_entries,
    get_entry_by_id,
    get_entry_by_username,
    update_entry_by_id,
    delete_entry_by_id,
    delete_entry_by_username,
)

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


# bcrypt.checkpw(users[username], bcrypt.hashpw(password.encode("utf-8"))
@app.route("/user", methods=["POST"])  # create new user
def create_user():
    user_data = UserSchema().load(request.get_json())

    username = request.json.get('username', None)

    pwd = request.json.get('password', None)
    hashed_pwd = bcrypt.hashpw(pwd.encode("utf-8"), bcrypt.gensalt())
    user_data.update({"password": hashed_pwd})
    user_data.update({"password": pwd})
    users[username] = pwd

    return create_entry(User, UserSchema, **user_data)


# curl -X POST -H "Content-Type:application/json" --data-binary "{\"username\": \"Pax1\", \"password\": \"abcdefg\"}" http://localhost:5000/user


@app.route("/user", methods=["GET"])  # get all users
@auth.login_required
def get_user():
    cur_user = auth.current_user()
    print(cur_user)
    return jsonify(UserSchema().dump(session.query(User).filter_by(username=cur_user.username).first()))


# curl -X GET -u Pax1:abcdefg http://localhost:5000/user


@app.route("/user/<int:id>", methods=["GET"])  # get user by id
@auth.login_required
def get_user_by_id(id):
    cur_user = auth.current_user()
    print(cur_user)
    if cur_user.id == id:
        return get_entry_by_id(User, UserSchema, id)
    else:
        raise InvalidUsage("Object not found", status_code=404)


@app.route("/user/<string:username>", methods=["GET"])  # get user by username
@auth.login_required
def get_user_by_username(username):
    cur_user = auth.current_user()
    print(cur_user)
    if cur_user.username == username:
        return get_entry_by_username(User, UserSchema, username)
    else:
        raise InvalidUsage("Object not found", status_code=404)


@app.route("/user/<int:id>", methods=["PUT"])  # update user by id
@auth.login_required
def update_user_by_id(id):
    cur_user = auth.current_user()
    print(cur_user)
    if cur_user.id == id:
        user_data = UserSchema().load(request.get_json())
        return update_entry_by_id(User, UserSchema, id, **user_data)
    else:
        raise InvalidUsage("Object not found", status_code=404)


# curl -X PUT -u Pax1:abcdefg -H "Content-Type:application/json" --data-binary "{\"first_name\": \"Ivan\"}" http://localhost:5000/user/5

@app.route("/user/<int:id>", methods=["DELETE"])  # delete user by id
@auth.login_required
def delete_user_by_id(id):
    cur_user = auth.current_user()
    print(cur_user)
    if id == int(cur_user.id):
        return delete_entry_by_id(User, UserSchema, id)
    else:
        raise InvalidUsage("Object not found", status_code=404)

# curl -X DELETE -u Pax2:abcdefg http://localhost:5000/user/1


@app.route("/user/<string:username>", methods=["DELETE"])  # delete user by username
@auth.login_required
def delete_user_by_username(username):
    cur_user = auth.current_user()
    print(cur_user)
    if cur_user.username == username:
        return delete_entry_by_username(User, UserSchema, username)
    else:
        raise InvalidUsage("Invalid entered value", status_code=404)

