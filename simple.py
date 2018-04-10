#!/usr/bin/python3

import sys, time, pyaudio, wave
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
        begin = 0
        end = 0

    def initUI(self):
        """TODO: Docstring for initUI.
        :returns: TODO

        """
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('Push', self)
        button.setToolTip('Push to create dots or dashs')
        button.move(100,70)
        button.pressed.connect(self.onPress)
        button.released.connect(self.onRelease)

        self.show()

    @pyqtSlot()
    def onPress(self):
        self.begin = time.time()

    @pyqtSlot()
    def onRelease(self):
        self.end = time.time()
        if (self.end - self.begin) < 0.15:
            print("woof")

        else:
            print("dog")


if __name__ == "__main__":
    chunk = 1024
    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())

        
