# Author: Guðjón Ingi Valdimarsson
# Date: 16.01.2020
import unittest

class Streets():
    def __init__(self):
        self.streets = []

    def addStreet(self, street):
        self.streets.append(street)
    
    def getStreetList(self):
        return self.streets
    
    def getAllStreets(self, neighbourhoodStr = ""):
        streetsStr = ""
        for street in self.streets:
            if street.neighbourhood == neighbourhoodStr:
                streetsStr += street.name + ","
        streetsStr = streetsStr[:-1]
        return streetsStr
    
    def getNeighbourhood(self, streetString = ""):
        neighbourhoodStr = ""
        for street in self.streets:
            if street.name == streetString:
                neighbourhoodStr = street.neighbourhood
        return neighbourhoodStr

class Street():
    def __init__(self, name, neighbourhood):
        self.name = name
        self.neighbourhood = neighbourhood

class MyTest(unittest.TestCase):
    def addTest(self):
        s = Streets()
        s.addStreet(Street("Menntavegur 1", "Vatnsmýri"))
        self.assertEqual(1, len(s.getStreetList()))

    def getAllStreetsTest(self):
        s = Streets()
        s.addStreet(Street("Menntavegur 1", "Vatnsmýri"))
        s.addStreet(Street("Landsspítali", "Fossvogur"))     
        s.addStreet(Street("Eldofninn", "Fossvogur"))

        self.assertEqual("Menntavegur 1", s.getAllStreets("Vatnsmýri"))
    
    def getNeighbourhoodTest(self):
        s = Streets()
        s.addStreet(Street("Menntavegur 1", "Vatnsmýri"))
        self.assertEqual("Vatnsmýri", s.getNeighbourhood("Menntavegur 1"))
    
tester = MyTest()
tester.addTest()
tester.getAllStreetsTest()
tester.getNeighbourhoodTest()
