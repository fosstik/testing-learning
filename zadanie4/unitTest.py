import unittest
from fastapi.testclient import TestClient
from main import app
from fastapi import status
from product_service import products

class TestApp(unittest.TestCase):
    client: TestClient

    def setUp(self):
        self.client = TestClient(app=app)
        products.clear()  

    def test_create_product(self):
        response = self.client.post(
            '/products/create',
            params={
                "title": "test title",
                "description": "test desc",
                "reviews": ["review1", "review2"],
                "rating": 5
            }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), "Товар создан")

    def test_update_product(self):
        self.client.post(
            '/products/create',
            params={
                "title": "original title",
                "description": "original desc",
                "reviews": ["initial"],
                "rating": 3
            }
        )
        
        response = self.client.put(
            f'/products/update/{products[0].id}',
            params={
                "title": "updated title",
                "rating": 4
            }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["title"], "updated title")
        self.assertEqual(response.json()["rating"], 4)

    def test_update_product_invalid_rating(self):
        self.client.post(
            '/products/create',
            params={
                "title": "product",
                "description": "desc",
                "reviews": ["review"],
                "rating": 3
            }
        )
        
        response = self.client.put(
            f'/products/update/{products[0].id}',
            params={
                "rating": 6
            }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), "Оценка должна быть меньше или равна 5")

    def test_get_one_product(self):
        self.client.post(
            '/products/create',
            params={
                "title": "test product",
                "description": "test desc",
                "reviews": ["good"],
                "rating": 5
            }
        )
        
        response = self.client.get(f'/products/one/{products[0].id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["title"], "test product")
        self.assertEqual(response.json()["rating"], 5)

    def test_delete_product(self):
        self.client.post(
            '/products/create',
            params={
                "title": "product to delete",
                "description": "desc",
                "reviews": ["review"],
                "rating": 4
            }
        )
        
        response = self.client.delete(f'/products/delete/{products[0].id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), 'Продукт удалена')

    def test_get_nonexistent_product(self):
        response = self.client.get('/products/one/1231312')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_products(self):
        for i in range(3):
            self.client.post(
                '/products/create',
                params={
                    "title": f"product {i}",
                    "description": "desc",
                    "reviews": [f"review {i}"],
                    "rating": i + 1
                }
            )
        
        response = self.client.get('/products')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 3)
        self.assertEqual(response.json()[0]["title"], "product 0")

if __name__ == '__main__':
    unittest.main()