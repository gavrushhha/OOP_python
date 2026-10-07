"""Список космических миссий."""

from generalList import generalList
from mission import mission


class missionList(generalList):
    def appendItem(self, value):
        if isinstance(value, mission):
            generalList.appendItem(self, value)

    def createItem(self, code, name, agency=None, year=0, days=0, img=""):
        if code in self.getCodes():
            print("Миссия с кодом %s уже существует" % (code,))
        else:
            m = mission(code, name, agency, year, days, img)
            self.appendItem(m)
            return m

    def newItem(self, name, agency=None, year=0, days=0, img=""):
        m = mission(self.getNewCode(), name, agency, year, days, img)
        self.appendItem(m)
        return m
