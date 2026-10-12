from missioneditform import missionEditForm
from missionstable import missionsTable
from page import page


class missionPage(page):
    def __init__(self, library, parent=None):
        page.__init__(self, library=library, parent=parent)
        self.setTable(missionsTable(library=library, parent=parent))
        self.setForm(missionEditForm(library=library, parent=parent))
        self.setConnect()
