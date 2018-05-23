import csv
from ial3p3.tomograph import Tomograph
from ial3p3.LSE import LSE
from ial3p3.evolutiveAlgorithm import EvolutiveAlgorithm, Chromosome
from ial3p3.descentGradient import DescentGradient


def read_from_csv(path):
    tomographList = []
    with open(path) as csvFile:
        reader = csv.reader(csvFile, quoting=csv.QUOTE_NONNUMERIC)
        for linie in reader:
            id = linie[0]
            bonesStructures = linie[1:240]
            airIntrusions = linie[241:385]
            relativeLocations = linie[385]
            tm = Tomograph(id, bonesStructures, airIntrusions, relativeLocations)
            tomographList.append(tm)
    return tomographList


def leastSquare(path):
    tomographList = read_from_csv(path)
    lse = LSE(tomographList)
    result = lse.compute()
    for i in range(len(tomographList)):
        curent = tomographList[i]
        curentMatrix = result
        curentValue = 0

        curentValue = curentMatrix[0][0]
        bonesStructures = curent.getBoneStructures()
        airInclusions = curent.getAirInclusions()
        for contor in range(len(bonesStructures)):
            curentValue = curentValue + curentMatrix[contor+1][0] * bonesStructures[contor]
        for contor in range(len(airInclusions)):
            curentValue = curentValue + curentMatrix[contor+241][0] * airInclusions[contor]
        curent.setAI_relativeLocation(curentValue)

    for t in tomographList:
        print(t.getId()," ",t.getAI_relativeLocation())


def evolutiveAlgorithm(path):
    tomographList = read_from_csv(path)
    evolutiveAlgorithm = EvolutiveAlgorithm(100,10,tomographList)

    coefficients = evolutiveAlgorithm.solve()
    for i in range(len(tomographList)):
        current = tomographList[i]
        currentValue = coefficients[0]
        bonesStructures = current.getBoneStructures()
        airInclusions = current.getAirInclusions()
        for contor in range(len(bonesStructures)):
            currentValue = currentValue + coefficients[contor+1] * bonesStructures[contor]

        for contor in range(len(airInclusions)):
            currentValue = currentValue + coefficients[contor+241] * airInclusions[contor]
        current.setAI_relativeLocation(currentValue)

def descentGradient(path):
    tomographList = read_from_csv(path)
    descentGradient = DescentGradient(3000,tomographList, 0.0000005)

    coefficients = descentGradient.getCoefficients()

    for i in range(len(tomographList)):
        current = tomographList[i]
        currentValue = 0
        currentValue = coefficients[0]

        boneStructures = current.getBoneStructures()
        airInclusions = current.getAirInclusions()

        for contor in range(len(boneStructures)):
            currentValue = currentValue + coefficients[contor + 1] * boneStructures[contor]

        for contor in range(len(airInclusions)):
            currentValue = currentValue + coefficients[contor + 241] * airInclusions[contor]
        current.setAI_relativeLocation(currentValue)
        currentValue = (currentValue*100.0)/100.0
        current.setAI_relativeLocation(currentValue)

    for t in tomographList:
        print(t.getId()," ",t.getAI_relativeLocation())
