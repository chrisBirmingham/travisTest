class Dragon:
    def __init__(self, name, initStrength, initDefence):
        self.name = name
        self.strength = initStrength
        self.defence = initDefence

    def getName(self):
        return self.name

    def getStrength(self):
        return self.strength

    def getDefence(self):
        return self.defence

    def setStrength(self, change):
        self.strength += change

    def setDefence(self, change):
        self.defence += change
