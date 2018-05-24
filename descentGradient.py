

class DescentGradient:

    def __init__(self, numberOfIterations, tomographList, learningRate):
        self.__numberOfIterations = numberOfIterations
        self.__tomographList = tomographList
        self.__learningRate = learningRate
        self.__coefficients = [0 for i in range(385)]
        self.__error = 0

    def compute(self):
        for i in range(self.__numberOfIterations):
            gradients = [0 for x in range(385)]
            for tomograph in self.__tomographList:
                error = 0
                error = error + self.__coefficients[0]
                bonesStrucrures = tomograph.getBoneStructures()
                airInclusions = tomograph.getAirInclusions()

                for contor in range(len(bonesStrucrures)):
                    gradients[contor+1] = bonesStrucrures[contor]
                for contor in range(len(airInclusions)):
                    gradients[contor+241] = airInclusions[contor]

                error = error - tomograph.getRelativeLocations()
                for contor in range(len(bonesStrucrures)):
                    gradients[contor] = gradients[contor] + self.__learningRate * bonesStrucrures[contor]
                for contor in range(len(airInclusions)):
                    gradients[contor] = gradients[contor] + self.__learningRate * airInclusions[contor]
            for aux in range(385):
                self.__coefficients[aux] = self.__coefficients - gradients[aux]/(1.0 * len(self.__tomographList))

    def getCoefficients(self):
        return self.__coefficients
