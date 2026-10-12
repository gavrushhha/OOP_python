"""Комбобокс космонавтов, которых ещё нет в экипаже миссии."""

from dbcombobox import dbComboBox


class astronautCombo(dbComboBox):
    def update(self):
        self.clear()
        if self.getCurrentRec() is None:
            return
        m = self.getLibrary().getMission(self.getCurrentRec())
        if not m:
            return
        crew_codes = m.getAstronautCodes()
        for a in self.getLibrary().getAstronautList():
            if a.getCode() not in crew_codes:
                self.addItem(a.getCode(), a.getInfoStr())
