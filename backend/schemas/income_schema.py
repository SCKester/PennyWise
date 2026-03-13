from marshmallow import Schema, fields

class IncomeSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    source = fields.Str()
    amount = fields.Float()
    date_received = fields.Str()
