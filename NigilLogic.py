from PyQt6.QtWidgets import *
from NigilScreen import *


class NigilLogic(QMainWindow, Ui_NigilScreen):
    def __init__(self, candidates_window) -> None:
        """Sets up the gui for Nigil"s profile and gives functionality to the candidates button.
           nigil_progile_home_button calls the nigil_home function."""
        super().__init__()
        self.setupUi(self)
        self.candidates_window = candidates_window
        self.nigil_profile_home_button.clicked.connect(lambda: self.nigil_home())

    def nigil_home(self) -> None:
        """Hides Nigil's profile and shows the candidates screen"""
        self.hide()
        self.candidates_window.show()
