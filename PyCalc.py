import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QGridLayout,
    QVBoxLayout
)

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.setFixedSize(320, 430)
        self.expression = ""

        self.initializeUI()

    def initializeUI(self):
        # Экран калькулятора
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFont(QFont("Arial", 26))
        self.display.setMinimumHeight(70)

        # Кнопки
        grid = QGridLayout()
        grid.setSpacing(8)

        buttons = [
            ("C", 0, 0),
            ("⌫", 0, 1),
            ("(", 0, 2),
            (")", 0, 3),

            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),

            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),

            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),

            ("0", 4, 0),
            (".", 4, 1),
            ("=", 4, 2),
            ("+", 4, 3),
        ]

        for text, row, column in buttons:
            button = QPushButton(text)
            button.setMinimumHeight(55)
            button.setFont(QFont("Arial", 16))

            button.clicked.connect(
                lambda checked=False, value=text:
                self.button_clicked(value)
            )

            grid.addWidget(button, row, column)

    def setUpMainWindow(self):
        pass

app = QApplication(sys.argv)
window = mainWindow()
sys.exit(app.exec())