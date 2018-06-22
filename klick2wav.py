#!/usr/bin/env python3

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt5.uic import loadUi

from PyQt5 import QtGui

import os
import subprocess

import webbrowser


version = "0.1"



class MyQtApp(QDialog):

    def __init__(self):
        super(MyQtApp, self).__init__()
        loadUi("klick2wavgui.ui", self)
        self.setWindowTitle("klick2wav " + version)
        self.bpmBox.setCurrentIndex(6)
        self.synthBox.setCurrentIndex(0)
        self.samplerateBox.setCurrentIndex(4)



        #self.pushButton.released.connect(self.on_pushButton_clicked)



    @pyqtSlot()
    def on_pushButton_clicked(self):

        # file picker and command
        self.files_types = "WAV (*.wav);;All files (*.*)"
        self.filename = QFileDialog.getSaveFileName(self, "Export File", "export.wav", self.files_types)
        #self.filename = ["export.wav"]
        self.filenamecommand = " -W " + self.filename[0]

        #samplerate command
        self.sampleratecommand = " -r " + self.samplerateBox.currentText()

        #synth choice command
        self.synthcommand = " -s " + str(self.synthBox.currentIndex())

        #emphasing command
        self.emphasingoptions = [" ", " -e ", " -E "]
        self.emphasingindex = self.emphasingBox.currentIndex()
        self.emphasingcommand = self.emphasingoptions[self.emphasingindex]


        #final command
        command = "klick " + self.filenamecommand + self.emphasingcommand + self.synthcommand + self.sampleratecommand + " " + self.repeatBox.text() + " " + self.bpmBox.currentText()

        print("File exported!\n\n" + command)
        self.textEdit.setText("File exported!\n\n" + command)

        #os.system(command)
        subprocess.Popen(command, shell=True)





# Main App
app = QApplication(sys.argv)
widget = MyQtApp()
widget.show()
sys.exit(app.exec_())
