import unittest
from app.for_test import ForTest


class TestTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_test(self):
        self.assertTrue(True)

    def test_return_1(self):
        self.assertEqual(ForTest().return1(), 1)
