from marshmallow import post_load, Schema, fields
from models import user

#
# class UserData(Schema):
#     class Meta:
#         fields = ("id", "username")


def create_entry(model_class, **kwargs):
    return model_class(**kwargs)

class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String()
    # firstName = fields.String()
    # lastName = fields.String()
    # email = fields.String()
    # password = fields.String()
    # phone = fields.String()
    # userStatus = fields.Boolean()


    # @post_load
    # def make_user(self, data):
    #     return user(**data)
