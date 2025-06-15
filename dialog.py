import sys

import self
from PyQt5.QtWidgets import QApplication,QWidget, QPushButton, QVBoxLayout ,QHBoxLayout,QLabel,QDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class Purshare(QDialog):
    def __init__(self, price, on_buy, old):
        super().__init__()
        with open("style_dialogs.css", "r") as stylesheet:
            self.setStyleSheet(stylesheet.read())
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle('Покупка')
        self.setFixedSize(500,600)
        self.Description = QLabel("Ви купляете:")
        self.Description2 = QLabel(F"{old} + 1 кліків")
        self.Description3 = QLabel("Ви впевнені ?")
        self.button_yes = QPushButton("Так")
        self.button_no = QPushButton("Ні")
        self.button_no.clicked.connect(self.on_no)
        self.button_yes.clicked.connect(lambda : (on_buy(), self.accept()))
        layout.addWidget(self.Description)
        layout.addWidget(self.Description2)
        layout.addWidget(self.Description3)
        layout.addWidget(self.button_yes)
        layout.addWidget(self.button_no)
    def on_yes(self,clicks):
        if clicks >= 10:
            clicks -= 10

        self.accept()
    def on_no(self):
        self.reject()





