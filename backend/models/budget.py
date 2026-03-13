from db import db

class WeeklyBudget(db.Model):
    __tablename__ = "weekly_budget"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.String(20), nullable=False)
    end_date = db.Column(db.String(20), nullable=False)
    planned_income = db.Column(db.Float, default=0)
    planned_expenses = db.Column(db.Float, default=0)
    remaining = db.Column(db.Float, default=0)
