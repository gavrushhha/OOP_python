"""Космическая миссия."""

from astronautList import astronautList
from general import general


class mission(general):
    """
    Миссия: код, название, агентство, год, длительность (дни),
    фото/эмблема, экипаж (список космонавтов).
    """

    def __init__(self, code=0, name="", agency=None, year=0, days=0, img=""):
        general.__init__(self, code, name)
        self.__crew = astronautList()
        self.setAgency(agency)
        self.setDays(days)
        self.setYear(year)
        self.setImg(img)

    def setImg(self, value):
        self.__img = value

    def setAgency(self, value):
        self.__agency = value

    def setDays(self, value):
        self.__days = value

    def setYear(self, value):
        self.__year = value

    def getImg(self):
        return self.__img

    def getAgency(self):
        return self.__agency

    def getAgencyCode(self):
        if self.__agency:
            return self.__agency.getCode()

    def getAgencyName(self):
        if self.__agency:
            return self.__agency.getName()
        return ""

    def getAgencyShortName(self):
        if self.__agency:
            return self.__agency.getShortname()
        return ""

    def getDays(self):
        return self.__days

    def getYear(self):
        return self.__year

    def appendAstronaut(self, item):
        self.__crew.appendItem(item)

    def removeAstronaut(self, code):
        return self.__crew.removeItem(code)

    def clearCrew(self):
        self.__crew.clear()

    def getAstronaut(self, code):
        return self.__crew.findByCode(code)

    def getCrew(self):
        return self.__crew

    def getAstronautCodes(self):
        return self.__crew.getCodes()

    def getCrewInfoStr(self):
        return self.__crew.getInfoStr()

    def getInfoStr(self):
        """
        Сводка по миссии:
        Гагарин Ю. А. Восток-1 — Роскосмос, 1961. — 1 дн.
        """
        s = self.getCrewInfoStr()
        if s:
            s += " "
        s += "%s — %s, %s. — %s дн." % (
            self.getName(),
            self.getAgencyShortName(),
            str(self.getYear()),
            str(self.getDays()),
        )
        return s
