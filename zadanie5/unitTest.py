import unittest
from fastapi.testclient import TestClient
from main import app
from expense_service import items

class Test(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        items.clear()

    def test_create_income(self):
        resp = self.client.post("/transactions/", params={"amount":1000, "category":"Salary", "type":"income"})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.text, '"Транзакция создана"')

    def test_create_expense(self):
        resp = self.client.post("/transactions/", params={"amount":500, "category":"Food", "type":"expense"})
        self.assertEqual(resp.status_code, 200)

    def test_update(self):
        self.client.post("/transactions/", params={"amount":1000, "category":"Salary", "type":"income"})
        id = items[0].id
        resp = self.client.put(f"/transactions/{id}", params={"amount":2000, "category":"Updated"})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.text, '"Транзакция обновлена"')
        trans = self.client.get("/transactions").json()
        self.assertEqual(len(trans), 1)
        self.assertEqual(trans[0]["amount"], 2000)
        self.assertEqual(trans[0]["category"], "Updated")

    def test_delete(self):
        self.client.post("/transactions/", params={"amount":500, "category":"Food", "type":"expense"})
        id = items[0].id
        resp = self.client.delete(f"/transactions/{id}")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.text, '"Транзакция удалена"')

    def test_delete_missing(self):
        resp = self.client.delete("/transactions/123")
        self.assertEqual(resp.status_code, 404)

    def test_list(self):
        self.client.post("/transactions/", params={"amount":1000, "category":"Salary", "type":"income"})
        self.client.post("/transactions/", params={"amount":500, "category":"Food", "type":"expense"})
        resp = self.client.get("/transactions")
        self.assertEqual(len(resp.json()), 2)

    def test_stats_income(self):
        self.client.post("/transactions/", params={"amount":2000, "category":"Salary", "type":"income"})
        resp = self.client.get("/stats")
        self.assertEqual(resp.json()["total_income"], 2000)

    def test_stats_full(self):
        self.client.post("/transactions/", params={"amount":3000, "category":"Salary", "type":"income"})
        self.client.post("/transactions/", params={"amount":1000, "category":"Rent", "type":"expense"})
        resp = self.client.get("/stats")
        self.assertEqual(resp.json()["balance"], 2000)

if __name__ == '__main__':
    unittest.main()