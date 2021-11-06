from app import app

from schemas import (
    UserSchema)

from db_utils import (
    create_entry,
    get_entry_by_id,
    get_entry_by_username,
    update_entry_by_id,
    delete_entry_by_id,
)

from models import User

from flask import request, jsonify


@app.route("/user", methods=["POST"])  # create new user
def create_user():
    user_data = UserSchema().load(request.get_json())
    user_obj = create_entry(User, **user_data)
    return jsonify(UserSchema().dump(user_obj))


@app.route("/user", methods=["GET"])  # get all users
def get_user():
    user_array = User.query.all()
    return jsonify(UserSchema(many=True).dump(user_array))


@app.route("/user/<int:id>", methods=["GET"])  # get user by id
def get_user_by_id(id):
    user_obj = get_entry_by_id(User, id)
    return jsonify(UserSchema().dump(user_obj))


@app.route("/user/<string:username>", methods=["GET"])  # get user by username
def get_user_by_username(username):
    user_obj = get_entry_by_username(User, username)
    return jsonify(UserSchema().dump(user_obj))


@app.route("/user/<int:id>", methods=["PUT"])  # update user by username
def update_user_by_id(id):
    user_data = UserSchema().load(request.get_json())
    user_obj = update_entry_by_id(User, id, **user_data)
    return jsonify(UserSchema().dump(user_obj))


@app.route("/user/<int:id>", methods=["DELETE"])  # delete user by id
def delete_user_by_id(id):
    user_obj = delete_entry_by_id(User, id)
    return jsonify(UserSchema().dump(user_obj))


if __name__ == "__main__":
    app.run(debug=True)
