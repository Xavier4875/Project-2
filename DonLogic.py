from PyQt6.QtWidgets import *
from DonScreen import *

class DonLogic(QMainWindow, Ui_DonScreen):
    def __init__(self, candidates_window):
        super().__init__()
        self.setupUi(self)
        self.candidates_window = candidates_window
        self.don_profile_home_button.clicked.connect(lambda: self.don_home())

    def don_home(self):
        self.hide()
        self.candidates_window.show()
