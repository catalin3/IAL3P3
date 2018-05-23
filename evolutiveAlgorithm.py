import random
from utils import chance50

class EvolutiveAlgorithm:

    def __init__(self, populationSize, interations, data):
        self.__populationSize = populationSize
        self.__interations = interations
        self.__data = data
        self.__curentPopulation = [0 for i in range(populationSize)]

        for i in range(populationSize):
            self.__curentPopulation[i] = Chromosome(None, self.__data)

    def getData(self):
        return self.__data

    def select(self):
        A = random.randint(0,self.__populationSize-1)
        B = random.randint(0,self.__populationSize-1)

        if random.random() > 0.05 and self.__curentPopulation[A].getFitness() < self.__curentPopulation[B].getFitness():
            return self.__curentPopulation[A]
        return self.__curentPopulation[B]

    def crossOver(self, A, B):
        coefA = A.getCoefficients()
        coefB = B.getCoefficients()
        resCoef = [0 for  i in range(385)]

        for i in range(len(coefA)//2):
            resCoef[i] = coefA[i]
            resCoef[i+len(coefA)//2] = coefB[i+len(coefA)//2]
        return Chromosome(resCoef,self.__data)

    def mutation(self, X):
        for i in range(3):
            index = random.randint(0,385-1)
            coef = X.getCoefficients()
            coef[index] = coef[index] + (random.random() * chance50(1,-1))
            X.setCoeficients(coef)
        return X

    def iteration(self):
        newPopulation = [Chromosome(None, self.__data) for i in range(self.__populationSize)]
        for i in range(self.__populationSize):
            newPopulation[i] = self.mutation(self.crossOver(self.select(),self.select()))
        self.__curentPopulation = newPopulation

    def getBest(self):
        result = self.__curentPopulation[0]
        for i in range(self.__populationSize):
            if self.__curentPopulation[i].getFitness() < result.getFitness():
                result = self.__curentPopulation[i]
        return result

    def solve(self):
        for i in range(self.__interations):
            self.iteration()
            fit = 0
            for c in self.__curentPopulation:
                fit = fit + c.getFitness()
        return self.getBest().getCoefficients()




class Chromosome:

    def __init__(self, coefficients, data):
        #self.__coeficients = coefficients
        if  coefficients == None:
            self.__coefficients = [0 for x in range(385)]
            for i in range(385):
                self.__coefficients[i] = round(random.uniform(-5,5), 2)
        else:
            self.__coefficients = coefficients
        self.__fitness = None
        self.computeFitness(data)


    def computeFitness(self, data):
        for curent in data:
            curentValue = self.__coefficients[0]
            boneStructures = curent.getBoneStructures()
            airInclusions = curent.getAirInclusions()

            for i in range(len(boneStructures)):
                curentValue = curentValue + self.__coefficients[i+1] * boneStructures[i]

            for i in range(len(airInclusions)):
                curentValue = curentValue + self.__coefficients[i+len(boneStructures)+1] * boneStructures[i]

            v = curent.getRelativeLocations()
            self.__fitness = (curentValue-v)**2

    def getCoefficients(self):
        return self.__coefficients

    def setCoeficients(self, coef):
        self.__coefficients = coef

    def getFitness(self):
        return self.__fitness


