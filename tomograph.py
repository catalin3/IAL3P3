

class Tomograph:
    def __init__(self, id, boneStructures, airInclusions, relativeLocations):
        self.__id = id
        self.__boneStructures = boneStructures
        self.__airInclusins = airInclusions
        self.__relativeLocations = relativeLocations
        self.__AI_relativeLocation = None

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getBoneStructures(self):
        return self.__boneStructures

    def setBoneStructures(self, boneStructures):
        self.__boneStructures = boneStructures

    def getAirInclusions(self):
        return self.__airInclusins

    def setAirInclusions(self, airInclusions):
        self.__airInclusins = airInclusions

    def getRelativeLocations(self):
        return self.__relativeLocations

    def setRelativeLocations(self, relativeLocations):
        self.__relativeLocations = relativeLocations

    def getAI_relativeLocation(self):
        return self.__AI_relativeLocation

    def setAI_relativeLocation(self, AI_relativeLocation):
        self.__AI_relativeLocation = AI_relativeLocation