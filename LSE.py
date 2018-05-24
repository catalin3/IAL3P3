from inverse import Inverse

class LSE:
    def __init__(self, tomographList):
        self.__tomographList = tomographList
        w = len(tomographList)
        h = 385
        self.__x = [[0 for x in range(h)] for y in range(w)]
        self.__y = [0 for x in range(w)]

        for i in range(w):
            boneStructures = tomographList[i].getBoneStructures()
            airInclusions = tomographList[i].getAirInclusions()
            self.__x[i][0] = 1.0
            #print(self.__x[i][0])

            for contor in range(len(boneStructures)):
                self.__x[i][contor+1] = boneStructures[contor]

            for contor in range(len(airInclusions)):
                self.__x[i][contor+241] = airInclusions[contor]

                self.__y[i] = tomographList[i].getRelativeLocations()


    def compute(self):
        print("compute")
        inv = Inverse()
        r = inv.invert(self.__x)

        return r
