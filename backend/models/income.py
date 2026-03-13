from db import db

class Income(db.Model):
    __tablename__ = "income"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    source = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, default=0)
    date_received = db.Column(db.String(20))
