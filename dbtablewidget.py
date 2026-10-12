"""Таблица с привязкой строк к кодам записей каталога."""

from PyQt5.QtWidgets import QTableWidget

from libwidget import libWidget
from rowcode import rowCode


class dbTableWidget(QTableWidget, libWidget):
    def __init__(self, library, parent=None, header=None):
        if header is None:
            header = []
        QTableWidget.__init__(self, parent)
        libWidget.__init__(self, library)
        self.__rowCode = rowCode()
        self.setHeader(header)
        self.update()

    def setHeader(self, value):
        self.setColumnCount(len(value))
        self.setHorizontalHeaderLabels(value)

    def clearContents(self):
        self.__rowCode.clear()
        QTableWidget.clearContents(self)

    def getCodes(self):
        return self.__rowCode.getCodes()

    def getCurrentCode(self):
        return self.__rowCode.getCode(self.currentRow())

    def setCurrentCode(self, code):
        if code is not None:
            row = self.__rowCode.getRow(code)
            if row is not None:
                self.setCurrentCell(row, 0)

    def appendRowCode(self, row, code):
        self.__rowCode.appendRowCode(row, code)

    def update(self, code=0):
        self.clearContents()
        self.setData()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        if code:
            self.setCurrentCode(code)

    def setData(self):
        pass
