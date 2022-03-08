from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


class Expenses(BaseModel):
    amount: float
    category: Optional[str] = 'Otros'
    currency: Optional[str] = 'Ars'


app = FastAPI()


@app.post('/expenses/')
async def create_expenses(expenses: Expenses):
    expense_dict = expenses.dict()
    if expenses.amount:
        expense_dict.update({"expenses": expenses.amount})
    if expenses.category is None:
        expense_dict.update({"category": "Otros"})
    else:
        expense_dict.update({"category": expenses.category})
    return expenses