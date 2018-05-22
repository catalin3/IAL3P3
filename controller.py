import csv
from ial3p3.tomograph import Tomograph
from ial3p3.LSE import LSE


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
        curentMatrix = result[0]
        curentValue = 0

        curentValue = curentMatrix[0][0]
        bonesStructures = curent.getBoneStructures()
        airInclusions = curent.getAirInclusions()
        for contor in range(len(bonesStructures)):
            curentValue = curentValue + curentMatrix[contor+1][0] * bonesStructures[contor]
        for contor in range(len(airInclusions)):
            curentValue = curentValue + curentValue[contor+241][0] * airInclusions[contor]
        curent.setAI_relativeLocation(curentValue)

    for t in tomographList:
        print(t.getId() + " " + t.getAI_relativeLocation())
'''
public void leastSquare(){
        LSE lse=new LSE(tomographList);
        Matrix[] result=lse.compute();
        for (int i=0;i<tomographList.size();i++){
            Tomograph current=tomographList.get(i);
            Matrix currentMatrix=result[0];
            double currentValue=0;

            currentValue=currentMatrix.get(0,0);
            double[] boneStructures=current.getBoneStructures();
            double[] airInclusions=current.getAirInclusions();
            for (int contor=0;contor<boneStructures.length;contor++)
                currentValue+=currentMatrix.get(contor+1,0)*boneStructures[contor];
            for(int contor=0;contor<airInclusions.length;contor++)
                currentValue+=currentMatrix.get(contor+241,0)*airInclusions[contor];
            current.setAI_relativeLocation(currentValue);

        }
    }
'''