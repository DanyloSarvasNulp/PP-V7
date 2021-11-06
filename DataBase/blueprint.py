from app import app
#
# from schemas import (
#     UserSchema)
#
# from db_utils import (
#     create_entry,
#     get_entry_by_id,
#     get_entry_by_username,
#     update_entry_by_id,
#     delete_entry_by_id,
# )
#
# from models import User
#
# from flask import request, jsonify

import Blueprint.userRequests


if __name__ == "__main__":
    app.run(debug=True)
