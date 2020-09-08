import unittest
from workout_programs import Workouts


class WorkoutProgramsTestMethods(unittest.TestCase):
    def test_percentages(self):
        expected_value = 65
        return_value = Workouts(100)._get_percentages()
        self.assertEqual(expected_value, return_value[65])

    def test_fivethreeone_program(self):
        expected_value = 63
        return_value = Workouts(100).fivethreeone_program()
        self.assertEqual(expected_value, return_value["Week 2"][0][0])