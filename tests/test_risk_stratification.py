import unittest
from unittest.mock import Mock
from risk.risk_stratification import *

#TODO: create testing module or way to run all tests with one command

class RiskFactorAssessmentClassificationTestMethods(unittest.TestCase):
    def setUp(self):
        self.risk_classification = RiskFactorAssessmentClassification()

    def test_patient_risk_classification_low(self):
        value = 1
        return_value = self.risk_classification.patient_risk_classification(value)
        self.assertEqual(self.risk_classification._low_risk_category(value), return_value)

    def test_patient_risk_classification_moderate(self):
        value = 2
        return_value = self.risk_classification.patient_risk_classification(value)
        self.assertEqual(self.risk_classification._moderate_risk_category(value), return_value)

    def test_patient_risk_classification_high(self):
        value = 3
        return_value = self.risk_classification.patient_risk_classification(value)
        self.assertEqual(self.risk_classification._high_risk_category(value), return_value)

    def tearDown(self):
        self.risk_classification = None

class RiskFactorAssessmentTestMethods(unittest.TestCase):
    def setUp(self):
        self.mock = Mock()
        self.patient = RiskFactorAssessment(self.mock)

    def test_is_age_risk_true(self):
        self.mock._sex = 'male'
        self.mock._age = 65
        self.assertTrue(self.patient._is_age_risk())

    def test_is_familial_risk_true(self):
        self.mock._male_family_death_before_55 = True
        self.mock._female_family_death_before_65 = False
        self.assertTrue(self.patient._is_familial_risk())

    def test_is_systolic_risk_true(self):
        self.mock._systolic = 130
        self.assertTrue(self.patient._is_systolic_risk())

    def test_is_diastolic_risk_true(self):
        self.mock._diastolic = 85
        self.assertTrue(self.patient._is_diastolic_risk())

    def test_is_dyslipidemia_risk_true(self):
        self.mock._ldl = 200
        self.mock._hdl = 40
        self.mock._cholesterol = 100
        self.assertTrue(self.patient._is_dyslipidemia_risk())

    def test_is_pre_diabetes_risk_true(self):
        self.mock._fasting_glucose = 120
        self.assertTrue(self.patient._is_pre_diabetes_risk())

    def test_is_hdl_negative_risk_true(self):
        self.mock._hdl = 80
        self.assertTrue(self.patient._is_hdl_negative_risk())

    def test_is_age_risk_false(self):
        self.mock._sex = 'female'
        self.mock._age = 25
        self.assertFalse(self.patient._is_age_risk())

    def test_is_familial_risk_false(self):
        self.mock._male_family_death_before_55 = False
        self.mock._female_family_death_before_65 = False
        self.assertFalse(self.patient._is_familial_risk())

    def test_is_systolic_risk_false(self):
        self.mock._systolic = 100
        self.assertFalse(self.patient._is_systolic_risk())

    def test_is_diastolic_risk_false(self):
        self.mock._diastolic = 70
        self.assertFalse(self.patient._is_diastolic_risk())

    def test_is_dyslipidemia_risk_false(self):
        self.mock._ldl = 100
        self.mock._hdl = 80
        self.mock._cholesterol = 100
        self.assertFalse(self.patient._is_dyslipidemia_risk())

    def test_is_pre_diabetes_risk_false(self):
        self.mock._fasting_glucose = 80
        self.assertFalse(self.patient._is_pre_diabetes_risk())

    def test_is_hdl_negative_risk_false(self):
        self.mock._hdl = 10
        self.assertFalse(self.patient._is_hdl_negative_risk())

    def tearDown(self):
        self.mock = None
        self.patient = None
