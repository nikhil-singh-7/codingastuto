from marshmallow import fields, Schema

class EmployeeSerializer(Schema):
    name = fields.Str(required=True)
    location = fields.Str(required=True)
    organization_id = fields.Integer(required=True)

class EmployeeResponseSerializer(Schema):
    id = fields.Integer(required=True)
    name = fields.Str(required=True)
    location = fields.Str(required=True)
    organization_id = fields.Integer(required=True)
