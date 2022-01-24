
class Signal:
    def __init__(self, name, measurmnetTime, warning, samples):
        self.name = name
        self.measurmentTime = float(measurmnetTime)
        self.samples = samples
        self.warning = warning

    def toString(self):
        print("nazwa: " + str(self.name))
        print("czas badania: " + str(self.measurmentTime))
        print("próbki: " + str(self.samples))
        print("ostrzeżenie: " + str(self.warning))