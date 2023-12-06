from PyQt6.QtWidgets import *
from CandidatesScreen import *
from VictorLogic import *
from DonLogic import *
from NigilLogic import *


class CandidatesLogic(QMainWindow, Ui_CandidatesScreen):
    def __init__(self, main_window):
        """Sets up the gui for the candidate screen and gives functionality to the buttons.
           pushButton calls the candidates_home function.
           victor_profile_button calls the victor_screen function.
           don_profile_button calls the don_screen function.
           nigil_profile_button calls the nigil_screen function."""
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.pushButton.clicked.connect(lambda: self.candidates_home())
        self.victor_profile_button.clicked.connect(lambda: self.victor_screen())
        self.don_profile_button.clicked.connect(lambda: self.don_screen())
        self.nigil_profile_button.clicked.connect(lambda: self.nigil_screen())

    def candidates_home(self):
        """Hides the candidates screen and shows the main menu"""
        self.hide()
        self.main_window.show()

    def victor_screen(self):
        """Hides the candidates screen and shows Victor's profile"""
        self.hide()
        victor_window = VictorLogic(self)
        victor_window.show()

    def don_screen(self):
        """Hides the candidates screen and shows Don's profile."""
        self.hide()
        don_window = DonLogic(self)
        don_window.show()

    def nigil_screen(self):
        """Hides the candidates screen and shows Nigil's profile."""
        self.hide()
        nigil_window = NigilLogic(self)
        nigil_window.show()
