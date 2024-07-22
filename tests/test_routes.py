import unittest
from app.main import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_recommendations(self):
        response = self.app.get('/q2?user_id=123&type=retweet&phrase=hello&hashtag=example')
        self.assertEqual(response.status_code, 200)
        # Add more assertions to verify the response content

if __name__ == '__main__':
    unittest.main()
