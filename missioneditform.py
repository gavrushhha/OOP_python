"""Форма редактирования миссии."""

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QLabel, QLineEdit, QPushButton, QSpinBox, QVBoxLayout

from agencycombo import agencyCombo
from astronautcombo import astronautCombo
from astronautlistwidget import astronautListWidget
from editform import editForm


class missionEditForm(editForm):
    def __init__(self, parent=None, library=None):
        editForm.__init__(self, library=library, parent=parent)
        self.__pixlabel = QLabel()
        self.__nameEdit = QLineEdit()
        self.__imgEdit = QLineEdit()
        self.__imgButton = QPushButton("найти")
        self.__astronautListWidget = astronautListWidget(library=library)
        self.__removeButton = QPushButton("удалить")
        self.__astronautCombo = astronautCombo(library=library)
        self.__appendButton = QPushButton("добавить")
        self.__agencyCombo = agencyCombo(library=library)
        self.__yearSpin = QSpinBox()
        self.__yearSpin.setRange(1900, QtCore.QDate().currentDate().year() + 10)
        self.__daysSpin = QSpinBox()
        self.__daysSpin.setRange(0, 10000)

        self.addLabel("название", 0, 0)
        self.addNewWidget(self.__nameEdit, 0, 1)
        self.addLabel("эмблема", 1, 0)
        self.addNewWidget(self.__imgEdit, 1, 1)
        self.addNewWidget(self.__imgButton, 1, 2)
        self.addLabel("экипаж", 2, 0)
        self.addNewWidget(self.__astronautListWidget, 2, 1)
        self.addNewWidget(self.__removeButton, 2, 2)
        self.addNewWidget(self.__astronautCombo, 3, 1)
        self.addNewWidget(self.__appendButton, 3, 2)
        self.addLabel("агентство", 4, 0)
        self.addNewWidget(self.__agencyCombo, 4, 1)
        self.addLabel("год", 5, 0)
        self.addNewWidget(self.__yearSpin, 5, 1)
        self.addLabel("дни", 6, 0)
        self.addNewWidget(self.__daysSpin, 6, 1)

        pix_vbox = QVBoxLayout()
        pix_vbox.addWidget(self.__pixlabel)
        pix_vbox.addStretch(1)
        self.addLeftLayout(pix_vbox)

        self.__removeButton.clicked.connect(self.removeAstronaut)
        self.__appendButton.clicked.connect(self.appendAstronaut)
        self.__imgButton.clicked.connect(self.openImg)

        if self.getLibrary().getMissionList():
            self.setCurrentCode(self.getLibrary().getMissionList()[0].getCode())

    def openImg(self):
        filename = QFileDialog.getOpenFileName(self, "Open file", "./")[0]
        if filename:
            self.__imgEdit.setText(filename)
            self.__pixlabel.setPixmap(QPixmap(filename))

    def update(self):
        if self.getCurrentCode() in self.getLibrary().getMissionCodes():
            m = self.getLibrary().getMission(self.getCurrentCode())
            self.__nameEdit.setText(m.getName())
            self.__imgEdit.setText(m.getImg())
            self.__pixlabel.setPixmap(QPixmap(m.getImg()))
            self.__agencyCombo.setCurrentRec(self.getCurrentCode())
            self.__astronautListWidget.setCurrentRec(self.getCurrentCode())
            self.__astronautCombo.setCurrentRec(self.getCurrentCode())
            self.__yearSpin.setValue(m.getYear())
            self.__daysSpin.setValue(m.getDays())

    def removeAstronaut(self):
        code = self.__astronautListWidget.getCurrentCode()
        if code:
            self.__astronautListWidget.removeSelected()
            person = self.getLibrary().getAstronaut(code)
            if person:
                self.__astronautCombo.addItem(code, person.getInfoStr())

    def appendAstronaut(self):
        code = self.__astronautCombo.getCurrentCode()
        if code:
            self.__astronautCombo.removeItem(self.__astronautCombo.currentIndex())
            person = self.getLibrary().getAstronaut(code)
            if person:
                self.__astronautListWidget.addItem(code, person.getInfoStr())

    def editClick(self):
        m = self.getLibrary().getMission(self.getCurrentCode())
        if not m:
            return
        m.setName(self.__nameEdit.text())
        m.setImg(self.__imgEdit.text())
        m.clearCrew()
        for c in self.__astronautListWidget.getCodes():
            m.appendAstronaut(self.getLibrary().getAstronaut(c))
        agency_code = self.__agencyCombo.getCurrentCode()
        m.setAgency(self.getLibrary().getAgency(agency_code) if agency_code else None)
        m.setYear(self.__yearSpin.value())
        m.setDays(self.__daysSpin.value())

    def newClick(self):
        m = self.getLibrary().newMission("", None, 0, 0, "")
        self.setCurrentCode(m.getCode())

    def delClick(self):
        self.getLibrary().removeMission(self.getCurrentCode())
