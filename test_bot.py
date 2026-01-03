Unit tests
import unittest
from bot import BasicBot

class TestBot(unittest.TestCase):
    def test_bot_creation(self):
        bot = BasicBot("key", "secret")
        self.assertIsNotNone(bot)

if __name__ == "__main__":
    unittest.main()
