import unittest
from risk.value_validation import *

class ValidateValuesTestMethods(unittest.TestCase):
    def test_valueIsMaleFemale_success(self):
        person = "male"
        valueMaleFemale = ValidateValue(person).valueIsMaleFemale()
        self.assertEqual(person, valueMaleFemale)

    def test_valueIsPositiveInteger_success(self):
        number_value = 100
        valuePositiveInteger = ValidateValue(number_value).valueIsPositiveInteger()
        self.assertEqual(number_value, valuePositiveInteger)

    def test_valueYesNo_success(self):
        valueYesNo = ValidateValue('yes').valueIsYesNo()
        self.assertEqual(True, valueYesNo)

    def test_valueIsMaleFemale_fails(self):
        kitten = ValidateValue('kitten')
        self.assertRaises(ValueError, kitten.valueIsMaleFemale)

    def test_valueIsPositiveInteger_fails(self):
        negative = ValidateValue(-100)
        word = ValidateValue('hello')
        self.assertRaises(ValueError, negative.valueIsPositiveInteger)
        self.assertRaises(ValueError, word.valueIsPositiveInteger)

    def test_valueIsYesNo_fails(self):
        bloop = ValidateValue('bloop')
        self.assertRaises(ValueError, bloop.valueIsYesNo)
