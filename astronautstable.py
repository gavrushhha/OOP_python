"""Таблица космонавтов."""

from PyQt5.QtWidgets import QTableWidgetItem

from dbtablewidget import dbTableWidget


class astronautsTable(dbTableWidget):
    def __init__(self, library, parent=None):
        dbTableWidget.__init__(
            self,
            library=library,
            parent=parent,
            header=["фамилия", "имя", "отчество"],
        )

    def setData(self):
        self.setRowCount(len(self.getLibrary().getAstronautCodes()))
        r = 0
        for a in self.getLibrary().getAstronautList():
            self.setItem(r, 0, QTableWidgetItem(a.getSurname()))
            self.setItem(r, 1, QTableWidgetItem(a.getName()))
            self.setItem(r, 2, QTableWidgetItem(a.getSecname()))
            self.appendRowCode(r, a.getCode())
            r += 1
