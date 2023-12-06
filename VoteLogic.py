from VoteScreen import *
from PyQt6.QtWidgets import *
from mainLogic import *


class VoteLogic(QMainWindow, Ui_VoteScreen):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.vote_home_button.clicked.connect(lambda: self.vote_home())
        self.main_window = main_window

    def vote_home(self):
        self.hide()
        self.main_window.show()



