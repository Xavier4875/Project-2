from PyQt6.QtWidgets import *
from ResultsScreen import *


class ResultsLogic(QMainWindow, Ui_ResultsScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
