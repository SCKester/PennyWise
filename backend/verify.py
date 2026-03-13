from app import create_app
from db import db
from models.budget import WeeklyBudget
from models.income import Income
from models.savings import SavingsGoal

app = create_app()
app.app_context().push()

print("\nDATABASE VERIFICATION REPORT")
print("────────────────────────────────")

# Weekly Budgets
budgets = WeeklyBudget.query.all()
print(f"\nWeekly Budgets ({len(budgets)})")
if budgets:
    for b in budgets:
        print(f"  ID {b.id} | {b.start_date} → {b.end_date} | Income: ${b.planned_income} | Expenses: ${b.planned_expenses} | Remaining: ${b.remaining}")
else:
    print("  No weekly budgets found.")

# Incomes
incomes = Income.query.all()
print(f"\nIncome Records ({len(incomes)})")
if incomes:
    for i in incomes:
        print(f"  ID {i.id} | {i.source} | Amount: ${i.amount} | Date: {i.date_received}")
else:
    print("  No income records found.")

# Savings Goals
goals = SavingsGoal.query.all()
print(f"\nSavings Goals ({len(goals)})")
if goals:
    for g in goals:
        progress = (g.current_amount / g.target_amount * 100) if g.target_amount else 0
        print(f"  ID {g.id} | {g.goal_name} | Target: ${g.target_amount} | Saved: ${g.current_amount} | Progress: {progress:.1f}% | Priority: {g.priority_rank}")
else:
    print("  No savings goals found.")

print("\nVerification complete.\n")
