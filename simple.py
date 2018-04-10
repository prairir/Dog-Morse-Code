#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication)
from PyQt5.QtCore import pyqtSlot

""""""
class Window(QWidget):

    """Docstring for Window. """

    def __init__(self):
        """TODO: to be defined1. """
        super().__init__()
        self.title = 'Doggy Morse Code'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        """TODO: Docstring for initUI.
        :returns: TODO

        """
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('Push', self)
        button.setToolTip('Push to create dots or dashs')
        button.move(100,70)
        button.clicked.connect(self.onClick)

        self.show()

    @pyqtSlot()
    def onClick(self):
        print('woof woof')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())

        
