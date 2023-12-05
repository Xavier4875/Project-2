from PyQt6.QtWidgets import *

from MainMenu import *
from VoteLogic import *
from CandidatesLogic import *
from ResultsLogic import *


class MainLogic(QMainWindow, Ui_MainMenu):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.VoteScreenButton.clicked.connect(lambda: self.openVoteWindow())
        self.pushButton.clicked.connect(lambda: self.openCandidateWindow())
        self.pushButton_2.clicked.connect(lambda: self.openResultsWindow())

    def openVoteWindow(self):
        self.hide()
        self.voteWindow = VoteLogic(self)
        self.voteWindow.show()

    def openCandidateWindow(self):
        self.hide()
        self.CandidateWindow = CandidatesLogic(self)
        self.CandidateWindow.show()

    def openResultsWindow(self):
        self.hide()
        self.ResultsWindow = ResultsLogic(self)
        self.ResultsWindow.show()
