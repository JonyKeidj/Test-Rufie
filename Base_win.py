from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from instr import *

class BaseWin(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        self.setWindowTitle(txt_title)