class ValidateValues():
    _female_male = ['female', 'male']
    _yes_no = ['yes', 'no']

    def __init__(self, value):
        self._value = value

    def valueIsMaleFemale(self):
        if self._value in ValidateValues._female_male:
            return self._value
        else:
            raise Exception('Value must be "male" or "female"')

    def valueIsPositiveInteger(self):
        integer_value = int(self._value)
        if integer_value > 0:
            return integer_value
        else:
            raise Exception('Value must be a positive number')

    def valueIsYesNo(self):
        if self._value in ValidateValues._yes_no:
            return self._value
        else:
            raise Exception('Value must be "yes" or "no"')

class Patient(object):
    _female_male = ['female', 'male']
    _yes_no = ['yes', 'no']

    def __init__(self, sex, age, smoker, sedentary, male_family_death_before_55, female_family_death_before_65, systolic, diastolic, hypertensive, ldl, hdl, cholesterol, fasting_glucose):
        self._sex = ValidateValues(sex).valueIsMaleFemale()
        self._age = ValidateValues(age).valueIsPositiveInteger()
        self._smoker = ValidateValues(smoker).valueIsYesNo()
        self._sedentary = ValidateValues(sedentary).valueIsYesNo()
        self._male_family_death_before_55 = male_family_death_before_55
        self._female_family_death_before_65 = female_family_death_before_65
        self._systolic = ValidateValues(systolic).valueIsPositiveInteger()
        self._diastolic = ValidateValues(diastolic).valueIsPositiveInteger()
        self._hypertensive = ValidateValues(hypertensive).valueIsYesNo()
        self._ldl = ValidateValues(ldl).valueIsPositiveInteger()
        self._hdl = ValidateValues(hdl).valueIsPositiveInteger()
        self._cholesterol = ValidateValues(cholesterol).valueIsPositiveInteger()
        self._fasting_glucose = ValidateValues(fasting_glucose).valueIsPositiveInteger()

class RiskFactorAssessmentClassificationResults(object):
    def __init__(self, patient):
        self._patient = patient

    def patient_risk_classification(self):
        total_risk_factors = self.get_assessment_results()

        if total_risk_factors <= 1:
            return self.low_risk_category()

        if total_risk_factors <= 2:
            return self.moderate_risk_category()

        if total_risk_factors > 2:
            return self.high_risk_category()

    def get_assessment_results(self):
        number_of_risk_factors = RiskFactorAssessment(self._patient).add_risk_factors()
        return number_of_risk_factors

    def low_risk_category(self):
        print("You are at a low risk for cardiovascular disease")

    def moderate_risk_category(self):
        print("You are at a moderate risk for cardiovascular disease")

    def high_risk_category(self):
        print("You are at a high risk for cardiovascular disease")


class RiskFactorAssessment(object):
    def __init__(self, patient):
        self._patient = patient

    def add_risk_factors(self):
        count_risk_factors = [self.is_age_risk(), self.is_smoker_risk(), self.is_sedentary_risk(), self.is_familial_risk(), self.is_systolic_risk(), self.is_diastolic_risk(), self.is_hypertensive_risk(), self.is_dyslipidemia_risk(), self.is_pre_diabetes_risk()].count(True)
        count_negative_risk_factor = [self.is_hdl_negative_risk()].count(True)
        total = count_risk_factors - count_negative_risk_factor
        return total

    def is_age_risk(self):
        if (self._patient._sex == "male" and self._patient._age >= 45) or (self._patient._sex == "female" and self._patient._age >=55):
            return True
        else:
            return False

    def is_smoker_risk(self):
        if self._patient._smoker == "yes":
            return True
        else:
            return False

    def is_sedentary_risk(self):
        if self._patient._sedentary == "yes":
            return True
        else:
            return False

    def is_familial_risk(self):
        if self._patient._male_family_death_before_55 == "yes" or self._patient._female_family_death_before_65 == "yes":
            return True
        else:
            return False

    def is_systolic_risk(self):
        if self._patient._systolic >= 120:
            return True
        else:
            return False

    def is_diastolic_risk(self):
        if self._patient._diastolic >= 80:
            return True
        else:
            return False

    def is_hypertensive_risk(self):
        if self._patient._hypertensive == "yes":
            return True
        else:
            return False

    def is_dyslipidemia_risk(self):
        if self._patient._ldl > 130 or self._patient._hdl < 40 or self._patient._cholesterol > 200:
            return True
        else:
            return False

    def is_pre_diabetes_risk(self):
        if self._patient._fasting_glucose >= 100 and self._patient._fasting_glucose <= 126:
            return True
        else:
            return False

    def is_hdl_negative_risk(self):
        if self._patient._hdl > 60:
            return True
        else:
            return False
