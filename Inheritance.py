class Results:
    def __init__(self):
        self.__phy = 0
        self.__chem = 0
        self.__math = 0

# These are now properties and not methods = getters
    @property
    def Physics(self):
        return self.__phy
    @property
    def Chemistry(self):
        return self.__chem
    @property
    def Maths(self):
        return self.__math

    @property
    def ResultsTotal(self):
        return self.__phy + self.__chem + self.__math

# Setters
    @Physics.setter
    def Physics(self, mark):
        if mark >= 0 and mark <= 150:
            self.__phy = mark
        else:
            print('Physics Mark must be between 0 and 150')

    @Chemistry.setter
    def Chemistry(self, mark):
        if mark >= 0 and mark <= 150:
            self.__chem = mark
        else:
            print('Chemsitry Mark must be between 0 and 150')

    @Maths.setter
    def Maths(self, mark):
        if mark >= 0 and mark <= 150:
                self.__math = mark
        else:
            print('Maths Mark must be between 0 and 150')

Ryan = Results()
Ryan.Physics = 80
Ryan.Chemistry = 90
Ryan.Maths = 80

print(Ryan.Physics)
RyanResults = Ryan.ResultsTotal
print(RyanResults)
