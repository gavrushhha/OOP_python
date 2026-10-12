"""Виджет превью изображения и имени файла."""

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QWidget


class pixWidget(QWidget):
    def __init__(self, filename="", parent=None):
        QWidget.__init__(self, parent=parent)
        self.__hbox = QHBoxLayout()
        self.setLayout(self.__hbox)
        if filename:
            pix_label = QLabel()
            pix_label.setPixmap(
                QPixmap(filename).scaled(32, 32, QtCore.Qt.KeepAspectRatio)
            )
            self.__hbox.addWidget(pix_label)
            self.__hbox.addWidget(QLabel(filename))
            self.__hbox.addStretch()
