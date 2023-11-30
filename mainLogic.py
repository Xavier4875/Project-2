from PyQt6.QtWidgets import *

from MainMenu import *
from VoteLogic import *
from CandidatesLogic import *
from ResultsLogic import *



class mainLogic(QMainWindow, Ui_MainMenu):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.VoteScreenButton.clicked.connect(lambda: self.vote())
        self.pushButton.clicked.connect(lambda: self.candidate())
        self.pushButton_2.clicked.connect(lambda: self.results())

    def vote(self):
        self.openVoteWindow()
    def candidate(self):
        self.openCandidateWindow()
    def results(self):
        self.openResultsWindow()

    def openVoteWindow(self):
        voteWindow = VoteLogic()
        voteWindow.show()

    def openCandidateWindow(self):
        CandidateWindow = CandidatesLogic()
        CandidateWindow.show()

    def openResultsWindow(self):
        ResultsWindow = ResultsLogic()
        ResultsWindow.show()
