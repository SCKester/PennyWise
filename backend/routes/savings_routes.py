from flask import Blueprint, request, jsonify
from db import db
from models.savings import SavingsGoal

savings_bp = Blueprint("savings_bp", __name__)

# CREATE a new savings goal
@savings_bp.post("/")
def create_goal():
    data = request.get_json()
    try:
        user_id = data["user_id"]
        goal_name = data["goal_name"]
        target_amount = float(data.get("target_amount", 0))
        current_amount = float(data.get("current_amount", 0))
        priority_rank = int(data.get("priority_rank", 999))
    except (KeyError, ValueError):
        return jsonify({"error": "Invalid or missing fields"}), 400

    new_goal = SavingsGoal(
        user_id=user_id,
        goal_name=goal_name,
        target_amount=target_amount,
        current_amount=current_amount,
        priority_rank=priority_rank
    )
    db.session.add(new_goal)
    db.session.commit()
    return jsonify({
        "message": "Savings goal created successfully",
        "goal": {
            "id": new_goal.id,
            "goal_name": new_goal.goal_name,
            "progress": f"{(new_goal.current_amount / new_goal.target_amount * 100) if new_goal.target_amount else 0:.2f}%"
        }
    }), 201


# READ all savings goals
@savings_bp.get("/")
def list_goals():
    goals = SavingsGoal.query.order_by(SavingsGoal.priority_rank.asc()).all()
    data = [
        {
            "id": g.id,
            "user_id": g.user_id,
            "goal_name": g.goal_name,
            "target_amount": g.target_amount,
            "current_amount": g.current_amount,
            "priority_rank": g.priority_rank,
        }
        for g in goals
    ]
    return jsonify(data), 200


# UPDATE an existing goal
@savings_bp.patch("/<int:goal_id>")
def update_goal(goal_id):
    goal = SavingsGoal.query.get(goal_id)
    if not goal:
        return jsonify({"error": "Goal not found"}), 404

    data = request.get_json()
    for field in ["goal_name", "target_amount", "current_amount", "priority_rank"]:
        if field in data:
            setattr(goal, field, data[field])

    db.session.commit()
    return jsonify({
        "message": "Goal updated successfully",
        "goal": {
            "id": goal.id,
            "goal_name": goal.goal_name,
            "target_amount": goal.target_amount,
            "current_amount": goal.current_amount,
            "priority_rank": goal.priority_rank,
        }
    }), 200


# DELETE a savings goal
@savings_bp.delete("/<int:goal_id>")
def delete_goal(goal_id):
    goal = SavingsGoal.query.get(goal_id)
    if not goal:
        return jsonify({"error": "Goal not found"}), 404

    db.session.delete(goal)
    db.session.commit()
    return jsonify({"message": f"Goal {goal_id} deleted"}), 200
