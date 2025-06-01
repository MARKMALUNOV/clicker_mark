import sys

import self
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout ,QHBoxLayout,QLabel,QDialog
from dialog import Purshare
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class ImageButtonApp(QWidget):
    def __init__(self):
        super().__init__()
        self.Clicks = 0
        self.setWindowTitle('Clicker Kruglow')
        self.setFixedSize(500,600)
        with open("style.css", "r") as stylesheet:
            self.setStyleSheet(stylesheet.read())
        layout = QVBoxLayout()

        self.button_Upgrade = QPushButton("Прокачка")
        self.Click_Label = QLabel("Clicks:0")
        self.button = QPushButton()
        self.button.setIcon(QIcon('Click_Button.png'))
        self.button.setIconSize(QSize(400, 500))
        self.button.clicked.connect(self.on_click)
        self.button_Upgrade.clicked.connect(self.on_purshare)
        layout.addWidget(self.Click_Label)
        layout.addWidget(self.button_Upgrade)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def on_click(self):
        self.Clicks += 1
        self.Click_Label.setText(f"Clicks :{self.Clicks}")
    def on_purshare(self):
        Purshare(self,
                 self.Clicks,
                 1,
                 2).exec_()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageButtonApp()
    window.show()
    sys.exit(app.exec_())
