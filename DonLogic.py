from PyQt6.QtWidgets import *
from DonScreen import *


class DonLogic(QMainWindow, Ui_DonScreen):
    def __init__(self, candidates_window) -> None:
        """Sets up the gui for Don's profile and gives functionality to the candidates button.
           don_profile_home_button calls the don_home function."""
        super().__init__()
        self.setupUi(self)
        self.candidates_window = candidates_window
        self.don_profile_home_button.clicked.connect(lambda: self.don_home())

    def don_home(self) -> None:
        """Hides Don's profile and shows the candidates screen."""
        self.hide()
        self.candidates_window.show()
