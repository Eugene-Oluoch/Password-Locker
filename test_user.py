import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new = User("Eugene", "Redcarpet")

    def test_init(self):
        self.assertEqual(self.new.username, "Mark")
        self.assertEqual(self.new.password, "Redcarpet")

    def tearDown(self):
        User.users = []
