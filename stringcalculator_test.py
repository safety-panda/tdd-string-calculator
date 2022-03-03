import unittest
from stringcalculator import add

class TestStringCalculator(unittest.TestCase):

    def test_add_empty_string_return_zero(self):
        self.assertEqual(add(''), 0)

    def test_one_number_will_return_itself(self):
        self.assertEqual(add('2'), 2)
        self.assertEqual(add('24'), 24)
    
    def test_add_two_numbers_separated_by_comma(self):
        self.assertEqual(add('1,2'), 3)
        self.assertEqual(add('21,9'), 30)

    def test_add_supports_random_number_of_number_inputs(self):
        self.assertEqual(add('1,3,9,6'), 19)
        self.assertEqual(add('1,4,7,9,8,10,11,23'),73)