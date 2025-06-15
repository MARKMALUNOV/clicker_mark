import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QDialog, QLineEdit, QMessageBox

class Inversion(QDialog):
    def __init__(self, clics, win, defeat):
        super().__init__()
        with open("style_dialogs.css", "r") as stylesheet:
            self.setStyleSheet(stylesheet.read())
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle('Удача')
        self.setFixedSize(500, 600)

        self.win = win
        self.defeat = defeat

        self.Description = QLabel("Ви ставите кліки на удачу (Шанс виграшу 44%)")
        self.dia_box = QLineEdit()
        self.dia_box.setPlaceholderText("Вкажіть кліки")
        self.yes_button = QPushButton("Так")
        self.no_button = QPushButton("Ні")

        self.yes_button.clicked.connect(self.on_yes)
        self.no_button.clicked.connect(self.on_no)

        layout.addWidget(self.Description)
        layout.addWidget(self.dia_box)
        layout.addWidget(self.yes_button)
        layout.addWidget(self.no_button)

    def on_yes(self):
        try:
            clics = int(self.dia_box.text())
        except ValueError:
            QMessageBox.warning(self, "Помилка", "Будь ласка, введіть коректну кількість кліків (число).")
            return

        chance = random.randint(0, 99)

        # 44% chance to win
        if chance < 44:
            QMessageBox.information(self, "Вітаємо!", f"Ви виграли! Ваші кліки: {clics}")
            self.win(clics)
            self.accept()
        else:
            QMessageBox.information(self, "Нам шкода", "Ви програли, спробуйте ще раз!")
            self.reject()
            self.defeat(clics)

    def on_no(self):
        self.reject()