

class BMIRiskCalculator(object):

    """
    BMI Risk Calculator
    """

    __TableData = {
        "BMICategory": ["Underweight", "Normal weight", "Overweight", "Moderately obese", "Severely obese", "Very severely obese"],
        "BMIRanges": [18.4, 24.9, 34.9, 39.9, 40], # note: ranges should be maintained in ascending order else it can be sorted while instantiating
        "HealthRisk": ["Malnutrition risk", "Low risk", "Enhanced risk", "Medium risk", "High risk", "Very high risk"]
    }

    __ReqDataFields = ["HeightCm","WeightKg"]

    def __init__(self):
        self.__vProcessedData = list()
        self.__vFaultData = list()
        self.__simple = list()     

    def _Calculate(self, pInputRec):
        height_mt = pInputRec['HeightCm']/100
        pInputRec['BMI'] = round(pInputRec['WeightKg']/(height_mt * height_mt), 1)

        if (pInputRec['BMI'] >= BMIRiskCalculator.__TableData['BMIRanges'][-1]):
                pInputRec['BMICategory'] = BMIRiskCalculator.__TableData['BMICategory'][-1]
                pInputRec['HealthRisk'] = BMIRiskCalculator.__TableData['HealthRisk'][-1]
        else:
            for c, r in enumerate(BMIRiskCalculator.__TableData['BMIRanges']):
                if (pInputRec['BMI'] <= r):
                    pInputRec['BMICategory'] = BMIRiskCalculator.__TableData['BMICategory'][c]
                    pInputRec['HealthRisk'] = BMIRiskCalculator.__TableData['HealthRisk'][c]
                    break
        self.__vProcessedData.append(pInputRec)

    def CheckRecStructure(self, pInputRec):
        for i in BMIRiskCalculator.__ReqDataFields:
            if i not in pInputRec:
                return False
        return True

    def Calculate(self, *pInputRecs):
        for rec in pInputRecs:
            if (self.CheckRecStructure(rec)):
                self._Calculate(rec)
            else:
                self.__vFaultData.append(rec)

    def GetFaultData (self):
        for i in self.__vFaultData:
            yield i

    def GetProcessedData (self):
        for i in self.__vProcessedData:
            yield i

    def GetNumPeopleWithCategory (self, pBMICategory):
        cnt = 0
        if pBMICategory not in BMIRiskCalculator.__TableData['BMICategory']:
            return cnt
        for i in self.__vProcessedData:
            if i['BMICategory'] == pBMICategory:
                cnt += 1
        return cnt

    def GetNumPeopleWithRisk (self, pHealthRisk):
        cnt = 0
        if pHealthRisk not in BMIRiskCalculator.__TableData['HealthRisk']:
            return cnt
        for i in self.__vProcessedData:
            if i['HealthRisk'] == pHealthRisk:
                cnt += 1
        return cnt



if __name__ == '__main__':

    InputData1 = [
        { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
        {"Gender": "Female", "HeightCm": 150, "WeightK": 70},
        {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
    ]

    InputData2 = [
        {"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
        { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
        { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }
    ]

    bmi_calc = BMIRiskCalculator()

    bmi_calc.Calculate (*InputData1)
    bmi_calc.Calculate (*InputData2)

    for i in bmi_calc.GetProcessedData():
        print(i)

    print("People with over weight: ", bmi_calc.GetNumPeopleWithCategory("Overweight"))

    for i in bmi_calc.GetFaultData():
        print(i)