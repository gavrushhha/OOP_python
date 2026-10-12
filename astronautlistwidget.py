"""Список космонавтов выбранной миссии."""

from dblistwidget import dbListWidget


class astronautListWidget(dbListWidget):
    def update(self):
        self.clear()
        if self.getCurrentRec() is None:
            return
        m = self.getLibrary().getMission(self.getCurrentRec())
        if not m:
            return
        crew = m.getCrew().getItems()
        for a in crew:
            self.addItem(a.getCode(), a.getInfoStr())
        if crew:
            self.setCurrentRow(0)
