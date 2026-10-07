"""Список космонавтов (экипаж миссии)."""

from astronaut import astronaut
from generalList import generalList


class astronautList(generalList):
    def appendItem(self, item):
        if not isinstance(item, astronaut):
            raise TypeError("В astronautList можно добавлять только astronaut")
        generalList.appendItem(self, item)

    def createItem(self, code, surname="", name="", secname=""):
        if code in self.getCodes():
            print("Космонавт с кодом %s уже существует" % (code,))
        else:
            item = astronaut(code, surname, name, secname)
            self.appendItem(item)
            return item

    def newItem(self, surname="", name="", secname=""):
        item = astronaut(self.getNewCode(), surname, name, secname)
        self.appendItem(item)
        return item

    def getInfoStr(self):
        """Экипаж через запятую: 'Гагарин Ю. А., Титов Г. С.'"""
        return ", ".join(item.getInfoStr() for item in self.getItems())
