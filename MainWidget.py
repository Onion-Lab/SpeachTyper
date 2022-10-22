from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *

from speachTyper import *

class MainWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi('MainWidget.ui', self)
        self.speachTyper = speachTyper(self)

        self.__initSlot()
        
        self.speachTyper.start()

        self.show()
        

    def __initSlot(self) :
        self.speachTyper.typeSpeachResultSignal.connect(self.typeSpeachResultSlot)
        

    def typeSpeachResultSlot(self, result) :
        TextEditContents = self.speachTextEdit.toPlainText()
        TextEditContents = TextEditContents + " " + result
        self.speachTextEdit.setText(TextEditContents)