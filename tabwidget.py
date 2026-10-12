from PyQt5.QtWidgets import QTabWidget

from agencypage import agencyPage
from astronautpage import astronautPage
from missionpage import missionPage


class tabWidget(QTabWidget):
    def __init__(self, library, parent=None):
        QTabWidget.__init__(self, parent)
        self.__missionPage = missionPage(library=library)
        self.addTab(self.__missionPage, "миссии")
        self.__astronautPage = astronautPage(library=library)
        self.addTab(self.__astronautPage, "космонавты")
        self.__agencyPage = agencyPage(library=library)
        self.addTab(self.__agencyPage, "агентства")
        self.currentChanged.connect(self.update)

    def update(self):
        self.__agencyPage.update()
        self.__astronautPage.update()
        self.__missionPage.update()
