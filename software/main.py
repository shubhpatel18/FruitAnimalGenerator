from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from software.widgets import ConfigWidget, GeneratorWidget

from software.app_data import AppData

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fruit Animal Generator")
        self.setWindowIcon(QIcon('resources/icon.ico'))
        self.setMinimumSize(QSize(500, 300))
        self.resize(QSize(600, 400))

        self.app_data = AppData()

        tab_widget = QTabWidget()
        tab_widget.addTab(GeneratorWidget(self.app_data), 'Generator')
        tab_widget.addTab(ConfigWidget(self.app_data), 'Config')
        self.setCentralWidget(tab_widget)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
