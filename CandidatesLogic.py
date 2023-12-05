from PyQt6.QtWidgets import *
from CandidatesScreen import *
from VictorLogic import *
from DonLogic import *
from NigilLogic import *

class CandidatesLogic(QMainWindow, Ui_CandidatesScreen):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.pushButton.clicked.connect(lambda: self.candidates_home())
        self.victor_profile_button.clicked.connect(lambda: self.victor_screen())
        self.don_profile_button.clicked.connect(lambda: self.don_screen())
        self.nigil_profile_button.clicked.connect(lambda: self.nigil_screen())

    def candidates_home(self):
        self.hide()
        self.main_window.show()

    def victor_screen(self):
        self.hide()
        victor_window = VictorLogic(self)
        victor_window.show()

    def don_screen(self):
        self.hide()
        don_window = DonLogic(self)
        don_window.show()

    def nigil_screen(self):
        self.hide()
        nigil_window = NigilLogic(self)
        nigil_window.show()
