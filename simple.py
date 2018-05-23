#!/usr/bin/python3

import sys, time, pyaudio, wave
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication)
from PyQt5.QtCore import pyqtSlot


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
        chunk=1024
        self.end = time.time()
        dog= wave.open("audio/dog.wav", 'rb')
        doggo= wave.open("audio/doggo.wav", 'rb')
        audio = pyaudio.PyAudio()

        streamd= audio.open(format=audio.get_format_from_width(dog.getsampwidth()),channels=dog.getnchannels(),rate=dog.getframerate(),output=True)
        streamdg= audio.open(format=audio.get_format_from_width(doggo.getsampwidth()),channels=doggo.getnchannels(),rate=doggo.getframerate(),output=True)
        datad=dog.readframes(chunk)
        datadg= doggo.readframes(chunk)
        
        if (self.end - self.begin) < 0.15:
            print("woof")
            while len(datad) > 0:
                streamd.write(datad)
                datad = dog.readframes(chunk)

            streamd.stop_stream()

        else:
            print("dog")

            while len(datadg) > 0:
                streamdg.write(datadg)
                datadg = doggo.readframes(chunk)

            streamdg.stop_stream()

        
        streamd.close()
        streamdg.close()
        audio.terminate()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = Window()
    sys.exit(app.exec_())

        
