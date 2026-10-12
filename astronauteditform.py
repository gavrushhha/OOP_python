"""Форма редактирования космонавта."""

from PyQt5.QtWidgets import QLineEdit

from editform import editForm


class astronautEditForm(editForm):
    def __init__(self, parent=None, library=None):
        editForm.__init__(self, library=library, parent=parent)
        self.__surnameEdit = QLineEdit()
        self.__nameEdit = QLineEdit()
        self.__secnameEdit = QLineEdit()
        self.addLabel("фамилия", 0, 0)
        self.addNewWidget(self.__surnameEdit, 0, 1)
        self.addLabel("имя", 1, 0)
        self.addNewWidget(self.__nameEdit, 1, 1)
        self.addLabel("отчество", 2, 0)
        self.addNewWidget(self.__secnameEdit, 2, 1)
        if self.getLibrary().getAstronautList():
            self.setCurrentCode(self.getLibrary().getAstronautList()[0].getCode())

    def update(self):
        if self.getCurrentCode() in self.getLibrary().getAstronautCodes():
            a = self.getLibrary().getAstronaut(self.getCurrentCode())
            self.__surnameEdit.setText(a.getSurname())
            self.__nameEdit.setText(a.getName())
            self.__secnameEdit.setText(a.getSecname())

    def editClick(self):
        a = self.getLibrary().getAstronaut(self.getCurrentCode())
        if a:
            a.setSurname(self.__surnameEdit.text())
            a.setName(self.__nameEdit.text())
            a.setSecname(self.__secnameEdit.text())

    def newClick(self):
        a = self.getLibrary().newAstronaut("", "", "")
        self.setCurrentCode(a.getCode())

    def delClick(self):
        self.getLibrary().removeAstronaut(self.getCurrentCode())
