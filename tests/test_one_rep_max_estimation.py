import unittest
from percentage_calculators.one_rep_max_estimation import *


class OneRepMaxEquationsTestMethods(unittest.TestCase):
    def test_one_rep_max_estimation(self):
        expected_value={'brzycki_formula': 100.0, 'epley_formula': 103.33333333333334, 'mayhew_formula': 108.86400361154962, 'lander_formula': 101.39029413020158, 'lombardi_formula': 100.0}
        return_value = one_rep_max_estimation(1,100)
        self.assertEqual(expected_value, return_value)

    def test_brzycki_formula(self):
        answer = 133.36889837289942
        return_value = OneRepMaxEquations(10, 100)._brzycki_formula()
        self.assertEqual(answer, return_value)

    def test_epley_formula(self):
        answer = 133.33333333333331
        return_value = OneRepMaxEquations(10, 100)._epley_formula()
        self.assertEqual(answer, return_value)

    def test_lander_formula(self):
        answer = 134.0703628078088
        return_value = OneRepMaxEquations(10, 100)._lander_formula()
        self.assertEqual(answer, return_value)

    def test_lombardi_formula(self):
        answer = 125.89254117941672
        return_value = OneRepMaxEquations(10, 100)._lombardi_formula()
        self.assertEqual(answer, return_value)
