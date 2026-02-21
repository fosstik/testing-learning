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

    def test_create_products(self):
        response = self.client.post(
            '/products/create',
            params={
                "title": "test title",
                "description": "test desc",
            }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), "Задача создана")

    def test_update_products(self):
        self.client.post(
            '/products/create',
            params={
                "title": "orig title",
            }
        )
        response = self.client.put(
            f'/products/update/{products[0].id}',
            params={
                "title": "update title",
                "complete":True
            }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_post(self):
        self.client.post(
            '/products/create',
            params={
                "title": "test post title",
            }
        )
        response = self.client.get(f'/products/one/{products[0].id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        self.client.post(
            '/products/create',
            params={
                "title": "delete products",
            }
        )
        response = self.client.delete(f'/products/delete/{products[0].id}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), 'Задача удалена')

    def test_post_not_found(self):
        response = self.client.get('/products/one/123')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_posts(self):
        self.client.post(
            '/products/create',
            params={
                "title": "products 1",
            }
        )
        response = self.client.get('/products')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

if __name__ == '__main__':
    unittest.main()