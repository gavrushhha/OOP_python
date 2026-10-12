from agenciestable import agenciesTable
from agencyeditform import agencyEditForm
from page import page


class agencyPage(page):
    def __init__(self, library, parent=None):
        page.__init__(self, library=library, parent=parent)
        self.setTable(agenciesTable(library=library, parent=parent))
        self.setForm(agencyEditForm(library=library, parent=parent))
        self.setConnect()
