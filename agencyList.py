"""Список космических агентств."""

from agency import agency
from generalList import generalList


class agencyList(generalList):
    def appendItem(self, value):
        if isinstance(value, agency):
            generalList.appendItem(self, value)

    def newItem(self, name, shortname=""):
        a = agency(self.getNewCode(), name, shortname)
        self.appendItem(a)
        return a

    def createItem(self, code, name, shortname=""):
        if code in self.getCodes():
            print("Агентство с кодом %s уже существует" % (code,))
        else:
            a = agency(code, name, shortname)
            self.appendItem(a)
            return a
