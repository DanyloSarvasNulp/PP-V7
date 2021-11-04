from app import app

from schemas import (
    UserSchema)

from db_utils import (
    create_entry,
    get_entry_by_username
)

from models import (
    Session,
    user)

from flask import request, jsonify


def dbconnect(func):
    def inner():
        with Session() as s:
            try:
                rez = func(session=s)
                s.commit()
                return rez
            except:
                s.rollback()
                return "ERROR: cannot create user"

    return inner


@app.route("/user", methods=["POST"])
@dbconnect
def create_user(session):
    user_data = UserSchema().load(request.get_json())
    user_obj = create_entry(user, **user_data)

    session.add(user_obj)

    return jsonify(UserSchema().dump(user_obj))


@app.route("/user", methods=["GET"])
def get_user():
    user_array = user.query.all()
    return jsonify(UserSchema(many=True).dump(user_array))


@app.route("/user/<string:username>")
def get_user_by_name(username):
    user_obj = get_entry_by_username(user, username)
    return jsonify(UserSchema().dump(user_obj))

if __name__ == "__main__":
    app.run(debug=True)
