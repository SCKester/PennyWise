from flask import Blueprint, request, jsonify
from db import db
from models.budget import WeeklyBudget

budget_bp = Blueprint("budget_bp", __name__)

# CREATE a new weekly budget
@budget_bp.post("/")
def create_weekly_budget():
    data = request.get_json()
    try:
        user_id = data["user_id"]
        start_date = data["start_date"]
        end_date = data["end_date"]
        planned_income = float(data.get("planned_income", 0))
        planned_expenses = float(data.get("planned_expenses", 0))
        remaining = planned_income - planned_expenses
    except (KeyError, ValueError):
        return jsonify({"error": "Invalid or missing fields"}), 400

    new_budget = WeeklyBudget(
        user_id=user_id,
        start_date=start_date,
        end_date=end_date,
        planned_income=planned_income,
        planned_expenses=planned_expenses,
        remaining=remaining,
    )
    db.session.add(new_budget)
    db.session.commit()
    return jsonify({
        "message": "Weekly budget created successfully",
        "budget": {
            "id": new_budget.id,
            "user_id": new_budget.user_id,
            "remaining": new_budget.remaining
        }
    }), 201


# READ all weekly budgets
@budget_bp.get("/")
def list_weekly_budgets():
    budgets = WeeklyBudget.query.all()
    data = [
        {
            "id": b.id,
            "user_id": b.user_id,
            "start_date": b.start_date,
            "end_date": b.end_date,
            "planned_income": b.planned_income,
            "planned_expenses": b.planned_expenses,
            "remaining": b.remaining,
        }
        for b in budgets
    ]
    return jsonify(data), 200
