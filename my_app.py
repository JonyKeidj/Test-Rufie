# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QLabel, QPushButton, 
    QVBoxLayout, QHBoxLayout, 
    QRadioButton)
from instr import *
from Base_win import *
from second_win import * 

class MainWidget(BaseWin):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
        self.connect()

    def initUI(self):
        self.hello = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        
        self.line = QVBoxLayout()
        
        self.line.addWidget(self.hello)
        self.line.addWidget(self.instruction)
        self.line.addWidget(self.button, alignment = Qt.AlignCenter)

        self.setLayout(self.line)

    def connect(self):
        self.button.clicked.connect(self.nextClick)


    def nextClick(self):
        self.hide()
        self.window_2 = SecondWin()
        
app = QApplication([])

window = MainWidget()

app.exec_()