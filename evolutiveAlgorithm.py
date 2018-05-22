import random
from ial3p3.utils import chance50

class EvolutiveAlgorithm:

    def __init__(self, populationSize, interations, data):
        self.__populationSize = populationSize
        self.__interations = interations
        self.__data = data
        self.__curentPopulation = [0 for i in range(populationSize)]

        for i in range(populationSize):
            self.__curentPopulation[i] = Chromosome(None, None)

    def getData(self):
        return self.__data

    def select(self):
        A = random.randint(0,self.__populationSize)
        B = random.randint(0,self.__populationSize)

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
        return Chromosome.constrChromosome(resCoef)

    def mutation(self, X):
        for i in range(3):
            index = random.randint(0,385)
            X.getCoefficients()[index] = X.getCoefficients()[index] + (random.random() * chance50(1,-1))
        return X

    def iteration(self):
        newPopulation = [Chromosome(None,None) for i in range(self.__populationSize)]
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
    # def constrChromosome(self, coefficients, data):
    #    self.__coeficients = coefficients
    #    self.computeFitness(data)

    def __init__(self, coefficients, data):
        if data == None and coefficients == None:
            self.__coeficients = [0 for x in range(385)]
            for i in range(385):
                self.__coeficients[i] = round(random.uniform(-5,5), 2)
        else:
            self.__coeficients = coefficients
            self.computeFitness(data)
        self.__fitness = None

    def computeFitness(self, data):
        for curent in data:
            curentValue = self.__coefficients[0]
            boneStructures = curent.getBoneStructures()
            airInclusions = curent.getAirInclusions()

            for i in range(len(boneStructures)):
                curentValue = curentValue + self.__coeficients[i+1] * boneStructures[i]

            for i in range(len(airInclusions)):
                curentValue = curentValue + self.__coeficients[i+len(boneStructures)+1] * boneStructures[i]

            v = curent.getRelativeLocation()
            self.__fitness = (curentValue-v)**2

    #def constrChromosome(self, coefficients, data):
    #    self.__coeficients = coefficients
    #    self.computeFitness(data)

    def getCoefficints(self):
        return self.__coeficients

    def getFitness(self):
        return self.__fitness


