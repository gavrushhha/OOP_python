"""Космическое агентство."""

from general import general


class agency(general):
    """Агентство: код, полное и краткое название."""

    def __init__(self, code=0, name="", shortname=""):
        general.__init__(self, code, name)
        self.setShortname(shortname)

    def setShortname(self, value):
        self.__shortname = value

    def getShortname(self):
        return self.__shortname
