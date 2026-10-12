from astronauteditform import astronautEditForm
from astronautstable import astronautsTable
from page import page


class astronautPage(page):
    def __init__(self, library, parent=None):
        page.__init__(self, library=library, parent=parent)
        self.setTable(astronautsTable(library=library, parent=parent))
        self.setForm(astronautEditForm(library=library, parent=parent))
        self.setConnect()
