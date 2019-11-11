from bot.functions import *
import unittest


def generate(arg="en_US"):
    response = ""
    faker = Faker(arg)
    response += faker.name() + "\n"
    response += str(random.randint(18, 60)) + "\n"
    response += faker.job() + "\n"
    response += faker.address()
    return response


def ping():
    return "pong"


class FunctionsTest(unittest.TestCase):
    def test_generate(self):
        self.assertNotEqual("", generate())

    def test_ping(self):
        self.assertEqual("pong", ping())

    def test_ping_not_one(self):
        self.assertIsNotNone(ping())

    def test_generate_not_none(self):
        self.assertIsNotNone(generate())


if __name__ == '__main__':
    unittest.main()
