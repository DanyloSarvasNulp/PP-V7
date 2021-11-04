from app import app

from schemas import (
    create_entry,
    UserSchema)

from models import (
    Session,
    user)

from flask import request, jsonify


def dbconnect(func):
    def inner(*args, **kwargs):
        with Session() as s:
            try:
                rez = func(*args, session=s, **kwargs)
                s.commit()
                return rez
            except:
                s.rollback()

    return inner


@app.route("/user", methods=["POST"])
@dbconnect
def create_user(*args, session, **kwargs):
    user_data = UserSchema().load(request.get_json())
    user_obj = create_entry(user, **user_data)
    session.add(user_obj)
    # with Session() as s:
    #     s.add(user_obj)
    #     s.commit()

    return UserSchema().dump(user_data)
    # return "", 200


if __name__  == "__main__":
    app.run(debug=True)