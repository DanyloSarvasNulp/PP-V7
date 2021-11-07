from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String()
    first_name = fields.String()
    last_name = fields.String()
    email = fields.String()
    password = fields.String()
    phone = fields.String()
    user_status = fields.Boolean()


class AuditoriumSchema(Schema):
    id = fields.Integer()
    auditorium_num = fields.Integer()
    max_people_count = fields.Integer()
    is_free = fields.Boolean()


class AccessSchema(Schema):
    auditorium_id = fields.Integer()
    user_id = fields.Integer()
    start = fields.DateTime()
    end = fields.DateTime()
