import unittest
from backend.app import create_app

class UserTestCase(unittest.TestCase):
    """
    Test case for user-related functionalities.
    """
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_get_users(self):
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)