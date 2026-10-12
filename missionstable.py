"""Таблица миссий."""

from PyQt5.QtWidgets import QTableWidgetItem

from dbtablewidget import dbTableWidget
from pixwidget import pixWidget


class missionsTable(dbTableWidget):
    def __init__(self, library, parent=None):
        dbTableWidget.__init__(
            self,
            library=library,
            parent=parent,
            header=["название", "эмблема", "экипаж", "агентство", "год", "дни"],
        )

    def setData(self):
        self.setRowCount(len(self.getLibrary().getMissionCodes()))
        r = 0
        for m in self.getLibrary().getMissionList():
            self.setItem(r, 0, QTableWidgetItem(m.getName()))
            self.setCellWidget(r, 1, pixWidget(m.getImg()))
            self.setItem(r, 2, QTableWidgetItem(m.getCrewInfoStr()))
            if m.getAgency():
                self.setItem(r, 3, QTableWidgetItem(m.getAgency().getName()))
            else:
                self.setItem(r, 3, QTableWidgetItem(""))
            self.setItem(r, 4, QTableWidgetItem(str(m.getYear())))
            self.setItem(r, 5, QTableWidgetItem(str(m.getDays())))
            self.appendRowCode(r, m.getCode())
            r += 1
