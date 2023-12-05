from PyQt6.QtWidgets import *
from ResultsScreen import *


class ResultsLogic(QMainWindow, Ui_ResultsScreen):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.results_home_button.clicked.connect(lambda: self.results_home())

    def results_home(self):
        self.hide()
        self.main_window.show()
