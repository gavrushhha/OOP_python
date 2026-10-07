"""Каталог космических данных: космонавты, агентства, миссии."""

from agencyList import agencyList
from astronautList import astronautList
from missionList import missionList


class cosmos:
    def __init__(self):
        self.__astronautList = astronautList()
        self.__agencyList = agencyList()
        self.__missionList = missionList()

    def clear(self):
        self.__missionList.clear()
        self.__astronautList.clear()
        self.__agencyList.clear()

    # --- космонавты ---
    def createAstronaut(self, code, surname, name="", secname=""):
        return self.__astronautList.createItem(code, surname, name, secname)

    def newAstronaut(self, surname, name="", secname=""):
        return self.__astronautList.newItem(surname, name, secname)

    def removeAstronaut(self, value):
        self.__astronautList.removeItem(value)
        for m in self.__missionList.getItems():
            m.removeAstronaut(value)

    def getAstronaut(self, code):
        return self.__astronautList.findByCode(code)

    def getAstronautList(self):
        return self.__astronautList.getItems()

    def getAstronautCodes(self):
        return self.__astronautList.getCodes()

    def getAstronautNewCode(self):
        return self.__astronautList.getNewCode()

    # --- агентства ---
    def createAgency(self, code, name, shortname=""):
        return self.__agencyList.createItem(code, name, shortname)

    def newAgency(self, name, shortname=""):
        return self.__agencyList.newItem(name, shortname)

    def removeAgency(self, code):
        self.__agencyList.removeItem(code)
        for m in self.__missionList.getItems():
            if m.getAgencyCode() == code:
                m.setAgency(None)

    def getAgency(self, code):
        return self.__agencyList.findByCode(code)

    def getAgencyList(self):
        return self.__agencyList.getItems()

    def getAgencyCodes(self):
        return self.__agencyList.getCodes()

    def getAgencyNewCode(self):
        return self.__agencyList.getNewCode()

    # --- миссии ---
    def createMission(self, code, name, agency=None, year=0, days=0, img=""):
        return self.__missionList.createItem(code, name, agency, year, days, img)

    def newMission(self, name, agency=None, year=0, days=0, img=""):
        return self.__missionList.newItem(name, agency, year, days, img)

    def removeMission(self, code):
        self.__missionList.removeItem(code)

    def getMission(self, code):
        return self.__missionList.findByCode(code)

    def getMissionList(self):
        return self.__missionList.getItems()

    def getMissionCodes(self):
        return self.__missionList.getCodes()

    def getMissionNewCode(self):
        return self.__missionList.getNewCode()
