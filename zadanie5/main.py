from fastapi import FastAPI, HTTPException
from expense_service import *

app = FastAPI()

@app.post("/transactions/")
def create(amount: float, category: str, type: str, date: str = None):
    add(amount, category, type, date)
    return "Транзакция создана"

@app.put("/transactions/{id}")
def edit(id: str, amount: float = None, category: str = None, type: str = None, date: str = None):
    if not update(id, amount, category, type, date):
        raise HTTPException(404, "Транзакция не найдена")
    return "Транзакция обновлена"

@app.delete("/transactions/{id}")
def remove(id: str):
    if not delete(id):
        raise HTTPException(404, "Транзакция не найдена")
    return "Транзакция удалена"

@app.get("/transactions")
def list_all():
    return get_all()

@app.get("/stats")
def calc_stats():
    return stats()