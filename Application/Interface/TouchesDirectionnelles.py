
from PyQt6.QtWidgets import  QWidget, QPushButton, QGridLayout
from PyQt6.QtGui import QPalette, QColor


class TouchesDirectionnelles(QWidget):
    def __init__(self, color):
        super(TouchesDirectionnelles, self).__init__()
        layout = QGridLayout()

        layout.addWidget(QPushButton("push1"), 0, 0)
        layout.addWidget(QPushButton("push2"), 0, 1)
        layout.addWidget(QPushButton("push3"), 0, 2)
        layout.addWidget(QPushButton("push4"), 1, 0)
        layout.addWidget(QPushButton("push5"), 1, 2)
        layout.addWidget(QPushButton("push6"), 2, 1)
        self.setLayout(layout)
