import unittest
from percentage_calculators.percentage_calculators import *


class MaxPercentageTestMethods(unittest.TestCase):
    def test_max_percentage(self):
        answer = 80
        return_value = percentage_value(80, 100)
        self.assertEqual(answer, return_value)
