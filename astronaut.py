"""Космонавт / астронавт."""

from general import general


class astronaut(general):
    """Космонавт: код, имя, фамилия, отчество."""

    def __init__(self, code=0, surname="", name="", secname=""):
        general.__init__(self, code, name)
        self.setSurname(surname)
        self.setSecname(secname)

    def setSurname(self, value):
        self.__surname = value

    def setSecname(self, value):
        self.__secname = value

    def getSurname(self):
        return self.__surname

    def getSecname(self):
        return self.__secname

    def getShortname(self):
        if self.getName():
            return self.getName()[0]
        return ""

    def getShortsecname(self):
        if self.getSecname():
            return self.getSecname()[0]
        return ""

    def getInfoStr(self):
        """Краткая запись: 'Гагарин Ю. А.'"""
        s = self.getSurname()
        if self.getShortname():
            s += " %s." % (self.getShortname(),)
        if self.getShortsecname():
            s += " %s." % (self.getShortsecname(),)
        return s
