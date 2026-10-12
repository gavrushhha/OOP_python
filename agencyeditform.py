"""Форма редактирования агентства."""

from PyQt5.QtWidgets import QLineEdit

from editform import editForm


class agencyEditForm(editForm):
    def __init__(self, parent=None, library=None):
        editForm.__init__(self, library=library, parent=parent)
        self.__nameEdit = QLineEdit()
        self.__shortnameEdit = QLineEdit()
        self.addLabel("название", 0, 0)
        self.addNewWidget(self.__nameEdit, 0, 1)
        self.addLabel("сокр. название", 1, 0)
        self.addNewWidget(self.__shortnameEdit, 1, 1)
        if self.getLibrary().getAgencyList():
            self.setCurrentCode(self.getLibrary().getAgencyList()[0].getCode())

    def update(self):
        if self.getCurrentCode() in self.getLibrary().getAgencyCodes():
            a = self.getLibrary().getAgency(self.getCurrentCode())
            self.__nameEdit.setText(a.getName())
            self.__shortnameEdit.setText(a.getShortname())

    def editClick(self):
        a = self.getLibrary().getAgency(self.getCurrentCode())
        if a:
            a.setName(self.__nameEdit.text())
            a.setShortname(self.__shortnameEdit.text())

    def newClick(self):
        a = self.getLibrary().newAgency("", "")
        self.setCurrentCode(a.getCode())

    def delClick(self):
        self.getLibrary().removeAgency(self.getCurrentCode())
