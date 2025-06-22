import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox
from dialog import Purshare
from dialog_inversion import Inversion
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import pygame
from dialog_settings import Settings
class ImageButtonApp(QWidget):
    def __init__(self):
        super().__init__()
        self.old = 1
        self.upgrades = 0
        self.upgrades_free = 10
        self.Clicks = 0
        self.clicks_plus = 1
        self.price = 10
        self.off_sound = 0
        self.on_sound = 100
        self.setWindowTitle('Клікер Круглов')
        self.setFixedSize(500, 650)
        pygame.init()
        pygame.mixer.init()

        try:
            with open("style.css", "r") as stylesheet:
                self.setStyleSheet(stylesheet.read())
        except FileNotFoundError:
            pass

        layout = QVBoxLayout()

        self.Click_Label = QLabel("Кліків: 0")
        self.sound1 = pygame.mixer.Sound('sounds/click_button_sound.wav')
        self.sound = pygame.mixer.Sound('sounds/click_sound.wav')
        self.button = QPushButton()
        self.button.setIcon(QIcon('images/Click_Button.png'))
        self.button.setIconSize(QSize(400, 500))
        self.button.clicked.connect(self.on_click)

        self.button_settings = QPushButton()
        self.button_settings.setIcon(QIcon('images/settings_button.png'))
        self.button.setIconSize(QSize(400, 500))
        self.button_settings.setFixedSize(50,50)

        self.button_Upgrade = QPushButton("Прокачка Кліків")
        self.button_inversion = QPushButton("Удача")

        self.button_Upgrade.clicked.connect(self.start)
        self.button_inversion.clicked.connect(self.start_1)
        self.button_settings.clicked.connect(self.on_settings)

        layout.addWidget(self.Click_Label)
        layout.addWidget(self.button_Upgrade)
        layout.addWidget(self.button_inversion)
        layout.addWidget(self.button)
        layout.addWidget(self.button_settings)
        self.setLayout(layout)

    def on_click(self):
        self.Clicks += self.clicks_plus
        self.sound.play()
        self.Click_Label.setText(f"Кліків :{self.Clicks}")

    def on_purshare(self):
        def on_accept_buy():
            if self.Clicks >= self.price:
                self.Clicks -= self.price
                self.plus_clicks()
                self.price += 10
                self.old += 1
                self.Click_Label.setText(f"Кліків :{self.Clicks}")
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Помилка :(")
                msg.setText("Не достатньо кліків або недостатньо місця :(")
                msg.exec_()

        Purshare(self.Clicks, on_accept_buy, self.old).exec_()

    def plus_clicks(self):
        self.clicks_plus += 1

    def on_inversion(self):
        if self.Clicks >= 30:
            def win(clics):
                self.Clicks *= 2
                self.Click_Label.setText(f"Кліків : {self.Clicks}")

            def defeat(clics):
                self.Clicks -= clics
                if self.Clicks < 0:
                    self.Clicks = 0
                self.Click_Label.setText(f"Кліків : {self.Clicks}")

            Inversion(self.Clicks, win, defeat).exec_()
        else:
            QMessageBox.warning(self,"Помилка","Ця функція заблокована (Нафармте 30 кліків)")

    def start(self):

        self.sound1.play()
        self.on_purshare()

    def start_1(self):
        self.sound1.play()
        self.on_inversion()

    def on_settings(self):
        def off_sound():
            self.sound.set_volume(0.0)
            self.sound1.set_volume(0.0)

        def on_sound():
            self.sound.set_volume(1)
            self.sound1.set_volume(1)

        Settings(off_sound,on_sound,self.change_sound).exec_()

    def change_sound(self,state):
        if state == 0 :
            state += 1
        else:
            state -= 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageButtonApp()
    window.show()
    sys.exit(app.exec_())