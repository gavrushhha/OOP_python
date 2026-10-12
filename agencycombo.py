"""Комбобокс выбора агентства миссии."""

from dbcombobox import dbComboBox


class agencyCombo(dbComboBox):
    def update(self):
        self.clear()
        if self.getCurrentRec() is None:
            return
        for a in self.getLibrary().getAgencyList():
            self.addItem(a.getCode(), a.getName())
        m = self.getLibrary().getMission(self.getCurrentRec())
        if m and m.getAgency():
            self.setCurrentCode(m.getAgency().getCode())
