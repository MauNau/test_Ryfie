from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import random
from PyQt5.QtGui import *

class SecondWindow(QWidget):
    def __init__ (self, *args, **qwargs):
        super().__init__(*args, **qwargs)
        self.initUI()

    def initUI(self):
        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        lable_name = QLabel('Введите ФИО')
        input_name = QLineEdit()
        input_name.setPlaceholderText('Иванов Иван Иванович')

        lable_age = QLabel('Полных лет:')
        input_age = QLineEdit()
        input_age.setPlaceholderText('32')

        lable_info1 = QLabel('Лягте на спину и замерте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", Чтобы запустить таймер')
        button_test1 = QPushButton('Начать первый тест')
        input_info1 = QLineEdit()
        input_info1.setPlaceholderText('0')

        lable_info2 = QLabel('')
        button_test2 = QPushButton('Начать делать приседания')

        lable_info3 = QLabel('')
        button_test3 = QPushButton('Начать финальный тест')
        input_info3 = QLineEdit()
        input_info3.setPlaceholderText('0')
        input_info4 = QLineEdit()
        input_info4.setPlaceholderText('0')

        button_result = QPushButton('Отправить результаты')

        left_layout.addWidget(lable_name, alignment=Qt.AlignLeft)
        left_layout.addWidget(input_name, alignment=Qt.AlignLeft)
        left_layout.addWidget(lable_age, alignment=Qt.AlignLeft)
        left_layout.addWidget(input_age, alignment=Qt.AlignLeft)
        left_layout.addWidget(lable_info1, alignment=Qt.AlignLeft)
        left_layout.addWidget(button_test1, alignment=Qt.AlignLeft)
        left_layout.addWidget(input_info1, alignment=Qt.AlignLeft)
        left_layout.addWidget(lable_info2, alignment=Qt.AlignLeft)
        left_layout.addWidget(button_test2, alignment=Qt.AlignLeft)
        left_layout.addWidget(lable_info3, alignment=Qt.AlignLeft)
        left_layout.addWidget(button_test3, alignment=Qt.AlignLeft)
        left_layout.addWidget(input_info3, alignment=Qt.AlignLeft)
        left_layout.addWidget(input_info4, alignment=Qt.AlignLeft)
        left_layout.addWidget(button_result)

        lable_timer = QLabel('00:00')

        right_layout.addWidget(lable_timer, alignment=Qt.AlignRight)

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)
        self.setLayout(main_layout)

app = QApplication([])
window = SecondWindow()
window.setFont(QFont('calibri', 15))
window.show()
app.exec_()