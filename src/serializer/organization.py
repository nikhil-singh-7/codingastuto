from marshmallow import fields, Schema

class OrganizationSerializer(Schema):
    name = fields.Str(required=True)
    location = fields.Str(required=True)
    category = fields.Str(required=True)