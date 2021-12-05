from DataBase.schemas import UserSchema
from DataBase.models import User
from flask_httpauth import HTTPBasicAuth
import bcrypt

from DataBase.db_utils import *

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    user = session.query(User).filter_by(username=username).first()

    if user and bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
        return user
    return False


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
            raise InvalidUsage("Object not found", status_code=404)  # pragma: no cover
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
