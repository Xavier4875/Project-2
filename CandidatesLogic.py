from PyQt6.QtWidgets import *
from CandidatesScreen import *

class CandidatesLogic(QMainWindow, Ui_CandidatesScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
