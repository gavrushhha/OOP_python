"""Задание 4. GUI PyQt5 для каталога космических миссий."""

import sys

from PyQt5.QtWidgets import QApplication

from mainwindow import mainWindow


def main():
    app = QApplication(sys.argv)
    mw = mainWindow()
    mw.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
