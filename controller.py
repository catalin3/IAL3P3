import csv
from tomograph import Tomograph
from LSE import LSE
from evolutiveAlgorithm import EvolutiveAlgorithm, Chromosome
from descentGradient import DescentGradient


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

        curentValue = curentMatrix[0][0]
        bonesStructures = curent.getBoneStructures()
        airInclusions = curent.getAirInclusions()
        for contor in range(len(bonesStructures)):
            curentValue = curentValue + curentMatrix[contor+1][0] * bonesStructures[contor]
        print(len(bonesStructures))
        print(len(airInclusions))
        for contor in range(len(airInclusions)):
            curentValue = curentValue + airInclusions[contor]
        curent.setAI_relativeLocation(curentValue)

    for t in tomographList:
        print(t.getId()," ",t.getAI_relativeLocation())


def evolutiveAlgorithm(path):
    print("evolutiveAlgorithm")
    tomographList = read_from_csv(path)
    print("read_from_csv")
    evolutiveAlgorithm = EvolutiveAlgorithm(10, 10, tomographList)
    print("evolutiveAlgorithm = EvolutiveAlgorithm")
    coefficients = evolutiveAlgorithm.solve()
    print("solve")
    for i in range(len(tomographList)):
        #print("aici for1")
        current = tomographList[i]
        currentValue = coefficients[0]
        bonesStructures = current.getBoneStructures()
        airInclusions = current.getAirInclusions()
        for contor in range(len(bonesStructures)):
            currentValue = currentValue + coefficients[contor+1] * bonesStructures[contor]
            #print("aici forBones")

        for contor in range(len(airInclusions)):
            currentValue = currentValue + coefficients[contor+241] * airInclusions[contor]
            #print("aici forAir")
        current.setAI_relativeLocation(currentValue)

    for t in tomographList:
        print(t.getId(), " ", t.getAI_relativeLocation())

def descentGradient(path):
    print("descentGradient")
    tomographList = read_from_csv(path)
    print("read_data")
    descentGradient = DescentGradient(3000, tomographList, 0.0000005)
    print("descentGradient = DescentGradient")
    coefficients = descentGradient.getCoefficients()
    print("coeficients")
    for i in range(len(tomographList)):
        current = tomographList[i]
        currentValue = coefficients[0]

        boneStructures = current.getBoneStructures()
        airInclusions = current.getAirInclusions()

        for contor in range(len(boneStructures)):
            currentValue = currentValue + coefficients[contor + 1] * boneStructures[contor]
        for contor in range(len(airInclusions)):
            currentValue = currentValue + airInclusions[contor]

        current.setAI_relativeLocation(currentValue)
        currentValue = round(currentValue*100.0)/100.0
        current.setAI_relativeLocation(currentValue)

    for t in tomographList:
        print(t.getId(), " ", t.getAI_relativeLocation())
