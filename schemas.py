from marshmallow import Schema, fields

class UserSchema(Schema):
    public_id = fields.String()
    firstname = fields.String()
    lastname = fields.String()
    username = fields.String()
    email = fields.String()
    