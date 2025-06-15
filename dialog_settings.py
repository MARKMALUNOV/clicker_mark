import sys

import self
from PyQt5.QtWidgets import QApplication,QWidget, QPushButton, QVBoxLayout ,QHBoxLayout,QLabel,QDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt

sound = 1
class Settings(QDialog):
    def __init__(self,funk,funk1):
        super().__init__()
        with open("style_dialogs.css", "r") as stylesheet:
            self.setStyleSheet(stylesheet.read())
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle('Налаштовування')
        self.setFixedSize(500,500)
        self.button_sound = QPushButton()
        self.button_sound.setIcon(QIcon('images/sound_button_on.png'))
        self.button_sound.setIconSize(QSize(70,70))
        self.button_sound.setFixedSize(QSize(70,70))
        self.button_sound.clicked.connect(lambda: self.sound(sound,funk,funk1))
        layout.addWidget(self.button_sound, alignment=Qt.AlignTop)


    def sound(self,on,funk,funk1):
        if on == 0:
            funk1()
            on = 1

        if on == 1:
            funk()
            on = 0









