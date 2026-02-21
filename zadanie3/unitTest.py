import unittest
from fastapi.testclient import TestClient
from main import app
from fastapi import status
from tasks_service import tasks

class TestApp(unittest.TestCase):
    client: TestClient

    def setUp(self):
        self.client = TestClient(app=app)
        tasks.clear()

    def test_create_task(self):
        response = self.client.post(
            '/task/create',
            params={
                "title": "test title",
            }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), "Задача создана")

    def test_update_task(self):
        self.client.post(
            '/task/create',
            params={
                "title": "orig title",
            }
        )
        response = self.client.put(
            f'/task/update/{tasks[0].id}',
            params={
                "title": "update title",
                "complete":True
            }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_post(self):
        self.client.post(
            '/task/create',
            params={
                "title": "test post title",
            }
        )
        response = self.client.get(f'/task/one/{tasks[0].id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        self.client.post(
            '/task/create',
            params={
                "title": "delete task",
            }
        )
        response = self.client.delete(f'/task/delete/{tasks[0].id}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), 'Задача удалена')

    def test_post_not_found(self):
        response = self.client.get('/task/one/123')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_posts(self):
        self.client.post(
            '/task/create',
            params={
                "title": "Task 1",
            }
        )
        response = self.client.get('/tasks')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

if __name__ == '__main__':
    unittest.main()