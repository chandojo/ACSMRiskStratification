# Exercise Coach Tools

This is a library of tools for fitness/exercise coaches, fitness specialists, exercise physiologists, and personal trainers to use.

## Table of Contents
1. [Getting Started](#gettingstarted)
2. [ACSM Risk Stratification](#acsmriskstratification)
3. [Percentage Calculators](#percentagecalculators)
4. [Testing](#testing)

## Getting Started <a name="gettingstarted"></a>
### Prerequisites

This package requires >= Python 3.7.4 and PyTest

### Installing

```
git clone https://github.com/chandojo/ACSMRiskStratification.git
```

## ACSM Risk Stratification <a name="acsmriskstratification"></a>
This is a tool for determining risk of cardiovascular disease based on *ACSM’s Guidelines for Exercise Testing and Prescription-8th ed. Philadelphia: Lippincott Williams & Wilkins*

This tool is not a substitute for advice from a doctor and is used to help fitness specialists refer potential clients to physicians due to possible cardiovascular health risk.

### Using the Stratification
A `Patient` object must pass through the class to use methods.

`Patient` takes the following parameters in the order listed:
- sex (str *male or female*)
- age (int *positive only*)
- smoker (str *yes or no*)
- sedentary (str *yes or no*)
- bmi (str *yes or no* ; input *0* if no available value but waist_girth value is available )
- waist_girth (int *positive only* ; input *0* if no available value but bmi value is available)
- male_family_death_before_55 (str *yes or no*)
- female_family_death_before_65 (str *yes or no*)
- systolic (int *positive only*)
- diastolic (int *positive only*)
- hypertensive (str *yes or no*)
- ldl (int *positive only*)
- hdl (int *positive only*)
- using_lipid_lowering_medication (str *yes or no*)
- cholesterol (int *positive only*)
- fasting_glucose (int *positive only* ; input *0* if no available value but oral_glucose_tolerance value is available)
- oral_glucose_tolerance (int *positive only* ; input *0* if no available value but fasting_glucose value is available)

**Useful functions:**
- `RiskFactorAssessment(patient).result_risk_classification()`
  - Returns patient's risk classification based off of the ACSM Guidelines. Classifications range from low, moderate, and high.
- `RiskFactorAssessment(patient).net_risk_factors()`
  - Returns patient's net total risk factors. This total is based off of ACSM's algorithm.


### Example
```
from risk.risk_stratification import RiskFactorAssessment

steve_buscemi = Patient('male', 61, 'no', 'yes', 25, 0, 'yes', 'no', 119, 78, 'no', 100, 70, 'no', 100, 60, 0)

RiskFactorAssessment(steve_buscemi).result_risk_classification()
# returns "Your risk total is 1. You are at a low risk for cardiovascular disease"

RiskFactorAssessment(steve_buscemi).net_risk_factors()
# returns 1

```

## Percentage Calculators <a name="percentagecalculators"></a>

**Useful functions:**
- `percentage_value(desired_percentage, 1_rep_max_weight)`
  - Returns weight value associated with desired percentage


### Example

```
from percentage_calculators.percentage_calculators import percentage_value

percentage_value(80, 100)
# returns 80
```

## Running the tests <a name="testing"></a>
```
python setup.py test
```

## Authors
chandojo
