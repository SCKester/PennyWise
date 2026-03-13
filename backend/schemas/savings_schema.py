from marshmallow import Schema, fields

class SavingsGoalSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    goal_name = fields.Str()
    target_amount = fields.Float()
    current_amount = fields.Float()
    priority_rank = fields.Int()
