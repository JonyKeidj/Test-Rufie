# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QLabel, QPushButton, 
    QVBoxLayout, QHBoxLayout, 
    QRadioButton, QLineEdit)
from Base_win import * 
from instr import *


class FinalWin(BaseWin):
    def __init__(self):
        super().__init__()
        self.show()
        self.initUI()

    def initUI(self):
        self.vline = QVBoxLayout()
        self.index = QLabel(txt_index)
        self.workheart = QLabel(txt_workheart)
        
        self.vline.addWidget(self.index)
        self.vline.addWidget(self.workheart)

        self.setLayout(self.vline)