import unittest
from stringcalculator import add

class TestStringCalculator(unittest.TestCase):

    def test_add_empty_string_return_zero(self):
        self.assertEqual(add(''), 0)

    def test_one_number_will_return_itself(self):
        self.assertEqual(add('2'), 2)
        self.assertEqual(add('24'), 24)