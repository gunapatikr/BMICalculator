
# Usage with example

'''
import BMICalculator import BMIRiskCaculator as BRC

# sample input data
InputData = [
        { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
        {"Gender": "Female", "HeightCm": 150, "WeightK": 70},
        {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
    ]

# Calulate the bmi fr the given above records and stores the data
bmi_calc = BRC.BMIRiskCalculator()
bmi_calc.Calculate (*InputData)

# Interface (instance method) to fetch all the records processed so far (yields dict)
for i in bmi_calc.GetProcessedData():
    print(i)

# Interface (instance method) to fetch all the fault records so far (yields dict)
for i in bmi_calc.GetFaultData():
    print(i)

# Interface (instance method) to fetch total count of people in a given category (returns int)
print("People with over weight: ", bmi_calc.GetNumPeopleWithCategory("Overweight"))

# Interface (instance method) to fetch total count of people having given health risk (returns int)
print("People with over weight: ", bmi_calc.GetNumPeopleWithRisk("Enhanced risk"))


'''


# Testing
