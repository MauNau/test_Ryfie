from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import random
from PyQt5.QtGui import *

class ResultWindow(QWidget):
    def __init__ (self, *args, **qwargs):
        super().__init__(*args, **qwargs)
        self.initUI()

    def initUI(self):
        self.main_layout = QVBoxLayout()

        self.name_lable = QLabel('тут будет ФИО')
        self.index_lable = QLabel('индекс руфье')
        self.result_lable = QLabel('работоспасобность сердца')

        self.main_layout.addWidget(self.name_lable, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.index_lable, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.result_lable, alignment=Qt.AlignCenter)

        self.setLayout(self.main_layout)

