from VoteScreen import *
from PyQt6.QtWidgets import *


class VoteLogic(QMainWindow, Ui_VoteScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


