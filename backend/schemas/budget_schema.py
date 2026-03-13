from marshmallow import Schema, fields

class WeeklyBudgetSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    start_date = fields.Str()
    end_date = fields.Str()
    planned_income = fields.Float()
    planned_expenses = fields.Float()
