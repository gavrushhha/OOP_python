"""Таблица агентств."""

from PyQt5.QtWidgets import QTableWidgetItem

from dbtablewidget import dbTableWidget


class agenciesTable(dbTableWidget):
    def __init__(self, library, parent=None):
        dbTableWidget.__init__(
            self,
            library=library,
            parent=parent,
            header=["название", "сокр. название"],
        )

    def setData(self):
        self.setRowCount(len(self.getLibrary().getAgencyCodes()))
        r = 0
        for a in self.getLibrary().getAgencyList():
            self.setItem(r, 0, QTableWidgetItem(a.getName()))
            self.setItem(r, 1, QTableWidgetItem(a.getShortname()))
            self.appendRowCode(r, a.getCode())
            r += 1
