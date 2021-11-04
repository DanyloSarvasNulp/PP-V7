from app import app

from schemas import (
    create_entry,
    UserSchema)
from models import Session
from models import user

from flask import request, jsonify


@app.route("/user", methods=["POST"])
def create_user():
    user_data = UserSchema().load(request.get_json())
    user_obj = create_entry(user, **user_data)

    with Session() as s:
        s.add(user_obj)
        s.commit()

    return UserSchema().dump(user_data)

    # return "", 200


if __name__  == "__main__":
    app.run(debug=True)