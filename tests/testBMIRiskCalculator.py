import unittest
from BMICalculator import BMIRiskCalculator as BRC



class TestBMIRiskCalculator (unittest.TestCase):

    def setUp(self):
        self.input = [
            {"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
            {"Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
            {"Gender": "Male", "HeightCm": 180, "WeightKg": 77 }
        ]

    def testCheckRecStructure(self):
        calc = BRC.BMIRiskCalculator()
        rslt1 = calc.CheckRecStructure({"Gender": "Male", "HeightCm": 171, "WeightKg": 96 })
        rslt2 = calc.CheckRecStructure({"Gender": "Male", "HeightCm": 171, "WeightKgs": 96 })
        self.assertTrue (rslt1, msg="Valid Record")
        self.assertFalse (rslt2, msg="InValid Record")


    def testCalculate(self):
        output = [
            {'Gender': 'Male', 'HeightCm': 171, 'WeightKg': 96, 'BMI': 32.8, 'BMICategory': 'Overweight', 'HealthRisk': 'Enhanced risk'},
            {'Gender': 'Male', 'HeightCm': 161, 'WeightKg': 85, 'BMI': 32.8, 'BMICategory': 'Overweight', 'HealthRisk': 'Enhanced risk'},
            {'Gender': 'Male', 'HeightCm': 180, 'WeightKg': 77, 'BMI': 23.8, 'BMICategory': 'Normal weight', 'HealthRisk': 'Low risk'}
        ]
        calc = BRC.BMIRiskCalculator()
        calc.Calculate(*self.input)
        for c, i in enumerate(calc.GetProcessedData()):
            self.assertEqual (i, output[c])


    def testGetNumPeopleWithCategory (self):
        calc = BRC.BMIRiskCalculator()
        calc.Calculate(*self.input)
        self.assertEqual(calc.GetNumPeopleWithCategory("Overweight"), 2)
        self.assertEqual(calc.GetNumPeopleWithCategory("overweight"), 0, msg = "Invalid Category should always be zero")


    def testGetNumPeopleWithRisk (self):
        calc = BRC.BMIRiskCalculator()
        calc.Calculate(*self.input)
        self.assertEqual(calc.GetNumPeopleWithRisk("Enhanced risk"), 2)
        self.assertEqual(calc.GetNumPeopleWithRisk("enhanced risk"), 0, msg = "Invalid Risk name should always be zero")


    def testGetFaultData (self):
        input = [
            {"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
            {"Gender": "Male", "HeightCm": 161, "WeightKgs": 85 }, # invalid record
            {"Gender": "Male", "HeightCm": 180, "WeightKg": 77 }
        ]
        calc = BRC.BMIRiskCalculator()
        calc.Calculate(*input)
        self.assertEqual(next(calc.GetFaultData()), input[1])
