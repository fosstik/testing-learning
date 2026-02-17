import unittest
from fastapi.testclient import TestClient
from main import app
from fastapi import status
from posts_service import posts

class TestApp(unittest.TestCase):
    client: TestClient

    def setUp(self):
        self.client = TestClient(app=app)
        posts.clear()

    def test_create_post(self):
        response = self.client.post(
            '/posts/create',
            params={
                "title": "test title",
                "description": "test desc",
                "comments": ["comm1", "comm2"]
            }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), "Запись создана")

    def test_update_post(self):
        self.client.post(
            '/posts/create',
            params={
                "title": "orig title",
                "description": "orig desc",
                "comments": ["orig comm1"]
            }
        )
        response = self.client.put(
            f'/posts/update/{posts[0].id}',
            params={
                "title": "update title",
                "description": "update desc",
                "comments": ["update comm1"]
            }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_post(self):
        self.client.post(
            '/posts/create',
            params={
                "title": "test post title",
                "description": "test post desc",
                "comments": ["comm"]
            }
        )
        response = self.client.get(f'/posts/one/{posts[0].id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        self.client.post(
            '/posts/create',
            params={
                "title": "delete post",
                "description": "delete post desc",
                "comments": ['delete coommm']
            }
        )
        response = self.client.delete(f'/posts/delete/{posts[0].id}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"detail": "Post deleted"})

    def test_post_not_found(self):
        response = self.client.get('/posts/one/123')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json(), {"detail": "Post not found"})

    def test_get_all_posts(self):
        self.client.post(
            '/posts/create',
            params={
                "title": "Post 1",
                "description": "First post",
                "comments": ["comment"]
            }
        )
        response = self.client.get('/posts')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

if __name__ == '__main__':
    unittest.main()