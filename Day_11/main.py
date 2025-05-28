import unittest

from Practice_11 import Database
from intergration_service import UserService

class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.db = Database()
        self.service = UserService(self.db)

    def test_register_and_fetch_user(self):
        self.service.register_user(1, "Alice")
        self.assertEqual(self.service.fetch_user(1), "ALice")

    def test_register_duplicate_user(self):
        self.service.register_user(2, "Bob")
        self.service.register_user(2, "Varun")

unittest.main(argv=[''], exit=False, verbosity=2)
