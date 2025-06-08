import sys

import self
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout ,QHBoxLayout,QLabel,QDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class Purshare(QDialog):
    def __init__(self, price, on_buy, old):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle('Purshare')
        self.setFixedSize(500,600)
        self.Description = QLabel("You purshare:")
        self.Description2 = QLabel(F"{old} * 2 clicks")
        self.Description3 = QLabel("You understand ?")
        self.button_yes = QPushButton("Yes")
        self.button_no = QPushButton("No")
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





