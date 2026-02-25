from expense_model import Transaction
from datetime import datetime

items = []

def get_all():
    return items

def get_one(id):
    for i in items:
        if i.id == id:
            return i
    return None

def add(amount, category, type, date=None):
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    i = Transaction(amount, category, type, date)
    items.append(i)
    return i

def update(id, amount=None, category=None, type=None, date=None):
    i = get_one(id)
    if i:
        if amount: i.amount = amount
        if category: i.category = category
        if type: i.type = type
        if date: i.date = date
        return i
    return None

def delete(id):
    i = get_one(id)
    if i:
        items.remove(i)
        return i
    return None

def stats():
    income = sum(i.amount for i in items if i.type == "income")
    expense = sum(i.amount for i in items if i.type == "expense")
    return {
        "total_income": income,
        "total_expense": expense,
        "balance": income - expense
    }