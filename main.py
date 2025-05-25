import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout ,QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class ImageButtonApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Кнопка-зображення')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.button_Upgrade = QPushButton("Прокачка")
        self.button = QPushButton()
        self.button.setIcon(QIcon('Click_Button.png'))
        self.button.setIconSize(QSize(400, 500))
        self.button.clicked.connect(self.on_click)

        layout.addWidget(self.button_Upgrade)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def on_click(self):
        print("Кнопка натиснута!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageButtonApp()
    window.show()
    sys.exit(app.exec_())
