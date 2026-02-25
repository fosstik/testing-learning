import uuid

class Transaction:
    def __init__(self, amount, category, type, date):
        self.id = str(uuid.uuid4())
        self.amount = amount
        self.category = category
        self.type = type
        self.date = date