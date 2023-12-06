from PyQt6.QtWidgets import *
from VictorScreen import *


class VictorLogic(QMainWindow, Ui_VictorScreen):
    def __init__(self, candidates_window):
        """Sets up the gui for Victor's profile and gives functionality to the candidates button.
           victor_profile_home_button calls the victor_home button."""
        super().__init__()
        self.setupUi(self)
        self.candidates_window = candidates_window
        self.victor_profile_home_button.clicked.connect(lambda: self.victor_home())

    def victor_home(self):
        """Hides Victor's profile and shows the candidates screen"""
        self.hide()
        self.candidates_window.show()
