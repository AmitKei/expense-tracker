from fastapi import FastAPI, Header, HTTPException
from app.models import Expense, ExpenseWithID
from app.database import add_expense, get_expenses, delete_expense, total_expenses, search_expenses

app = FastAPI()

def extract_user(x_username: str = Header(...)):
    if not x_username:
        raise HTTPException(status_code=400, detail="Username header missing")
    return x_username.lower()

@app.post("/expenses")
def create_expense(expense: Expense, username: str = Header(...)):
    user = extract_user(username)
    expense_id = add_expense(user, expense.dict())
    return {"message": "Expense added", "id": expense_id}

@app.get("/expenses")
def list_expenses(username: str = Header(...), search: Optional[str] = None):
    user = extract_user(username)
    if search:
        return search_expenses(user, search)
    return get_expenses(user)

@app.delete("/expenses/{expense_id}")
def remove_expense(expense_id: int, username: str = Header(...)):
    user = extract_user(username)
    deleted = delete_expense(user, expense_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Expense not found")
    return {"message": "Deleted"}

@app.get("/total")
def get_total(username: str = Header(...)):
    user = extract_user(username)
    return {"total": total_expenses(user)}
