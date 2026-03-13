# backend/seed.py
from app import create_app
from db import db
from models.income import Income
from models.budget import WeeklyBudget
from models.savings import SavingsGoal

app = create_app()
app.app_context().push()

# Clear existing data (optional)
db.session.query(Income).delete()
db.session.query(WeeklyBudget).delete()
db.session.query(SavingsGoal).delete()
db.session.commit()

# Add sample Weekly Budgets
b1 = WeeklyBudget(user_id=1, start_date="2025-11-01", end_date="2025-11-07", planned_income=1000, planned_expenses=400, remaining=600)
b2 = WeeklyBudget(user_id=1, start_date="2025-11-08", end_date="2025-11-14", planned_income=900, planned_expenses=350, remaining=550)

# Add sample Incomes
i1 = Income(user_id=1, source="Job", amount=1200, date_received="2025-11-01")
i2 = Income(user_id=1, source="Freelance Project", amount=450.75, date_received="2025-11-02")

# Add sample Savings Goals
s1 = SavingsGoal(user_id=1, goal_name="Emergency Fund", target_amount=1000, current_amount=250, priority_rank=1)
s2 = SavingsGoal(user_id=1, goal_name="Vacation", target_amount=800, current_amount=200, priority_rank=2)

# Add to session
db.session.add_all([b1, b2, i1, i2, s1, s2])
db.session.commit()

print("Database seeded successfully!")

import verify  # Automatically runs the verification after seeding
