from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import  QMainWindow, QHBoxLayout, QWidget
from Interface.TouchesDirectionnelles import TouchesDirectionnelles


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        touchesdirectionnelles = TouchesDirectionnelles('red')

        layout = QHBoxLayout()

        layout.addWidget(touchesdirectionnelles)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)