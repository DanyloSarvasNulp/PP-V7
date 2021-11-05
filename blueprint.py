from app import app

from schemas import (
    UserSchema)

from db_utils import (
    create_entry,
    get_entry_by_id,
    get_entry_by_username,
)

from models import (
    Session,
    user)

from flask import request, jsonify


# def dbconnect(func):
#     def inner(*args, **kwargs):
#         with Session() as s:
#             try:
#                 rez = func(session=s, *args, **kwargs)
#                 s.commit()
#                 return rez
#             except:
#                 s.rollback()
#                 return "ERROR: operation failed"
#
#     return inner


@app.route("/user", methods=["POST"])  # create new user
def create_user():
    user_data = UserSchema().load(request.get_json())
    user_obj = create_entry(user, **user_data)
    return jsonify(UserSchema().dump(user_obj))


@app.route("/user", methods=["GET"])  # get all users
def get_user():
    user_array = user.query.all()
    return jsonify(UserSchema(many=True).dump(user_array))


@app.route("/user/<int:id>", methods=["GET"])  # get user by id
def get_user_by_username(username):
    user_obj = get_entry_by_id(user, id)
    return jsonify(UserSchema().dump(user_obj))


@app.route("/user/<string:username>", methods=["GET"])  # get user by username
def get_user_by_username(username):
    user_obj = get_entry_by_username(user, username)
    return jsonify(UserSchema().dump(user_obj))


# @app.route("/user/<string:username>", methods=["DELETE"])
# @dbconnect
# def delete_user_by_username(session, username):
#     user_obj = get_entry_by_username(user, username)
#     # session.delete(user_obj)
#     return jsonify(UserSchema().dump(user_obj))


if __name__ == "__main__":
    app.run(debug=True)
