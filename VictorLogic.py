from PyQt6.QtWidgets import *
from VictorScreen import *

class VictorLogic(QMainWindow, Ui_VictorScreen):
    def __init__(self, candidates_window):
        super().__init__()
        self.setupUi(self)
        self.candidates_window = candidates_window
        self.victor_profile_home_button.clicked.connect(lambda: self.victor_home())

    def victor_home(self):
        self.hide()
        self.candidates_window.show()
