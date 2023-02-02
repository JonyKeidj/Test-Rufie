# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QLabel, QPushButton, 
    QVBoxLayout, QHBoxLayout, 
    QRadioButton, QLineEdit)
from Base_win import * 
from instr import *
from final_win import *

class SecondWin(BaseWin):
    def __init__(self):
        super().__init__()
        self.show()
        self.initUI()
        self.connect()

    def initUI(self):
        self.name = QLabel(txt_name)
        self.hintname = QLineEdit(txt_hintname)
        self.age = QLabel(txt_age)
        self.hintage = QLineEdit(txt_hintage)
        
        self.instruction_1 = QLabel(txt_test1)
        self.button_1 = QPushButton(txt_starttest1)
        self.test_1 = QLineEdit(txt_hinttest1)
        
        self.instruction_2 = QLabel(txt_test2)
        self.button_2 = QPushButton(txt_starttest2)
        
        self.instruction_3 = QLabel(txt_test3)
        self.button_3 = QPushButton(txt_starttest3)
        self.test_3 = QLineEdit(txt_hinttest2)
        self.test3 = QLineEdit(txt_hinttest3)

        self.resalt_button = QPushButton(txt_sendresults)

        self.line = QVBoxLayout()        
        self.line.addWidget(self.name)
        self.line.addWidget(self.hintname, alignment = Qt.AlignLeft)
        self.line.addWidget(self.age)
        self.line.addWidget(self.hintage, alignment = Qt.AlignLeft)
        self.line.addWidget(self.instruction_1)
        self.line.addWidget(self.button_1, alignment = Qt.AlignLeft)
        self.line.addWidget(self.test_1, alignment = Qt.AlignLeft)
        self.line.addWidget(self.instruction_2)
        self.line.addWidget(self.button_2, alignment = Qt.AlignLeft)
        self.line.addWidget(self.instruction_3)
        self.line.addWidget(self.button_3, alignment = Qt.AlignLeft)
        self.line.addWidget(self.test_3, alignment = Qt.AlignLeft)
        self.line.addWidget(self.test3, alignment = Qt.AlignLeft)
        self.line.addWidget(self.resalt_button, alignment = Qt.AlignCenter)

        self.setLayout(self.line)

    def connect(self):
        self.resalt_button.clicked.connect(self.nextClick)

    def nextClick(self):
        self.hide()
        self.final_window = FinalWin()