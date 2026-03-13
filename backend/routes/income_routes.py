from flask import Blueprint, request, jsonify
from db import db
from models.income import Income

income_bp = Blueprint("income_bp", __name__)

# CREATE a new income record
@income_bp.post("/")
def create_income():
    data = request.get_json()
    try:
        user_id = data["user_id"]
        source = data["source"]
        amount = float(data["amount"])
        date_received = data.get("date_received")
    except (KeyError, ValueError):
        return jsonify({"error": "Invalid or missing fields"}), 400

    new_income = Income(
        user_id=user_id,
        source=source,
        amount=amount,
        date_received=date_received
    )
    db.session.add(new_income)
    db.session.commit()
    return jsonify({
        "message": "Income added successfully",
        "income": {
            "id": new_income.id,
            "source": new_income.source,
            "amount": new_income.amount
        }
    }), 201


# READ all income records
@income_bp.get("/")
def list_incomes():
    incomes = Income.query.all()
    data = [
        {
            "id": i.id,
            "user_id": i.user_id,
            "source": i.source,
            "amount": i.amount,
            "date_received": i.date_received,
        }
        for i in incomes
    ]
    return jsonify(data), 200
