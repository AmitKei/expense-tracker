from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage
from typing import Optional

db = TinyDB(storage=MemoryStorage)

def get_user_table(username: str):
    return db.table(username)

def add_expense(username: str, expense_data: dict):
    return get_user_table(username).insert(expense_data)

def get_expenses(username: str):
    return get_user_table(username).all()

def delete_expense(username: str, expense_id: int):
    return get_user_table(username).remove(doc_ids=[expense_id])

def total_expenses(username: str):
    return sum(exp["amount"] for exp in get_expenses(username))

def search_expenses(username: str, keyword: str):
    ExpenseQ = Query()
    return get_user_table(username).search(ExpenseQ.description.matches(keyword, flags=8))  # flags=8 -> re.IGNORECASE
