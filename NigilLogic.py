from PyQt6.QtWidgets import *
from NigilScreen import *

class NigilLogic(QMainWindow, Ui_NigilScreen):
    def __init__(self, candidates_window):
        super().__init__()
        self.setupUi(self)
        self.candidates_window = candidates_window
        self.nigil_profile_home_button.clicked.connect(lambda: self.nigil_home())

    def nigil_home(self):
        self.hide()
        self.candidates_window.show()
