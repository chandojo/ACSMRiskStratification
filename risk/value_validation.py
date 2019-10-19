class ValidateValue():
    _female_male = ['female', 'male']
    _yes_no = {
                'yes': True,
                'no': False
                }

    def __init__(self, value):
        self._value = value

    def valueIsMaleFemale(self):
        if self._value in ValidateValue._female_male:
            return self._value
        else:
            raise ValueError('%s is an incorrect value. It must be male or female.' % self._value)

    def valueIsPositiveInteger(self):
        integer_value = int(self._value)
        if integer_value > 0:
            return integer_value
        else:
            raise ValueError('%s is an incorrect value. It must be a number and must higher than zero.' % self._value)

    def valueIsYesNo(self):
        if self._value in ValidateValue._yes_no.keys():
            return ValidateValue._yes_no[self._value]
        else:
            raise ValueError('%s is an incorrect value. Must be yes or no.' % self._value)
