from bot.bot_client import *
import unittest


class TestBotClient(unittest.TestCase):
    def test_client_returned_value(self):
        self.assertIsNotNone(get_bot())


if __name__ == '__main__':
    unittest.main()