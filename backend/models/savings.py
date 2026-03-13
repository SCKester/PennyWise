from db import db

class SavingsGoal(db.Model):
    __tablename__ = "savings_goal"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    goal_name = db.Column(db.String(100), nullable=False)
    target_amount = db.Column(db.Float, default=0)
    current_amount = db.Column(db.Float, default=0)
    priority_rank = db.Column(db.Integer, default=999)
