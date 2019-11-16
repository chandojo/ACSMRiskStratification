import unittest
from percentage_calculators.percentage_calculators import *


class PercentageCalculatorsTestMethods(unittest.TestCase):
    def test_percentage_value(self):
        answer = 80
        return_value = percentage_value(80, 100)
        self.assertEqual(answer, return_value)
