from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt

class Settings(QDialog):
    def __init__(self, funk, funk1, sound_state):
        super().__init__()
        with open("style_dialogs.css", "r") as stylesheet:
            self.setStyleSheet(stylesheet.read())

        self.sound_state = sound_state
        self.setWindowTitle('Налаштовування')
        self.setFixedSize(500, 500)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.button_sound = QPushButton()
        if self.sound_state == 1:
            self.button_sound.setIcon(QIcon('images/sound_button_on.png'))
        else:
            self.button_sound.setIcon(QIcon('images/sound_button_off.png'))
        self.button_sound.setIconSize(QSize(70, 70))
        self.button_sound.setFixedSize(QSize(70, 70))
        self.developer_button = QPushButton("Розробники")
        self.developer_button.setFixedSize(QSize(200, 70))

        self.button_sound.clicked.connect(lambda: self.toggle_sound(funk, funk1))

        layout.addWidget(self.button_sound, alignment=Qt.AlignTop)
        layout.addWidget(self.developer_button, alignment=Qt.AlignTop)

    def toggle_sound(self, funk, funk1):
        if self.sound_state == 0:
            funk1()
            self.button_sound.setIcon(QIcon('images/sound_button_on.png'))
            self.sound_state = 1
        else:
            funk()
            self.button_sound.setIcon(QIcon('images/sound_button_off.png'))
            self.sound_state = 0
