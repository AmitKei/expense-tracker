from pydantic import BaseModel
from typing import Literal

class Expense(BaseModel):
    description: str
    amount: float
    category: Literal["Food", "Transport", "Leisure", "Utilities", "Other"]

class ExpenseWithID(Expense):
    id: int
