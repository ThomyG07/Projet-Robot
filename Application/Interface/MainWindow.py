from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import  QMainWindow, QHBoxLayout, QWidget
from Interface.TouchesDirectionnelles import TouchesDirectionnelles
from Interface.SettingWidget import SettingWidget



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        

        self.setWindowTitle("My App")
        
        touchesdirectionnelles = TouchesDirectionnelles()
        settingwidget = SettingWidget(touchesdirectionnelles)

        layout = QHBoxLayout()

        layout.addWidget(touchesdirectionnelles)
        layout.addWidget(settingwidget)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)