# ACSM Risk Stratification

This is a tool for determining risk of cardiovascular disease based on *ACSM’s Guidelines for Exercise Testing and Prescription-8th ed. Philadelphia: Lippincott Williams & Wilkins*

This tool is not a substitute for advice from a doctor and is used to help fitness specialists refer potential clients to physicians due to possible cardiovascular health risk.

## Getting Started
### Prerequisites

This package requires >= Python 3.7.4 and PyTest

### Installing

```
git clone (repo link)
```

## Using the Stratification
A `Patient` object must pass through the class to use methods.

`Patient` takes the following parameters in the order listed:
- sex (str *male or female*)
- age (int *positive only*)
- smoker (str *yes or no*)
- sedentary (str *yes or no*)
- male_family_death_before_55 (str *yes or no*)
- female_family_death_before_65 (str *yes or no*)
- systolic (int *positive only*)
- diastolic (int *positive only*)
- hypertensive (str *yes or no*)
- ldl (int *positive only*)
- hdl (int *positive only*)
- cholesterol (int *positive only*)
- fasting_glucose (int *positive only*)

**Useful functions:**
- `RiskFactorAssessment(patient).result_risk_classification()`
  - Returns patient's risk classification based off of the ACSM Guidelines. Classifications range from low, moderate, and high.
- `RiskFactorAssessment(patient).net_risk_factors()`
  - Returns patient's net total risk factors. This total is based off of ACSM's algorithm.


### Example
```
steve_buscemi = Patient('male', 61, 'no', 'yes', 'yes', 'no', 119, 78, 'no', 100, 70, 100, 60)

RiskFactorAssessment(steve_buscemi).result_risk_classification()
# returns "Your risk total is 1. You are at a low risk for cardiovascular disease"

RiskFactorAssessment(steve_buscemi).net_risk_factors()
# returns 1

```

## Running the tests
```
python setup.py test
```

## Authors
chandojo
