from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to Expense Tracker API!"
    }

class Expense(BaseModel):
    id: int
    title: str
    category: str
    amount: float

expense = Expense(
    id=1,
    title="Lunch",
    category="Food",
    amount=200
)

print(expense)

expenses = []

@app.post("/expenses")
def add_expense(expense: Expense):
    expenses.append(expense)

    return {
        "message": "Expense added successfully!",
        "expense": expense
    }

@app.get("/expenses")
def get_expenses():
    return expenses

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):

    for expense in expenses:
        if expense.id == expense_id:
            expenses.remove(expense)

            return {
                "message": "Expense deleted successfully!"
            }

    return {
        "message": "Expense not found!"
    }