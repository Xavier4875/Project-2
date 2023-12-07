from PyQt6.QtWidgets import *

from MainMenu import *
from VoteLogic import *
from CandidatesLogic import *
from ResultsLogic import *


class MainLogic(QMainWindow, Ui_MainMenu):

    def __init__(self) -> None:
        """Sets up the gui and gives functionality to the buttons on the main menu.
           VoteScreenButton calls the openVoteWindow function.
           pushButton calls the openCandidateWindow function.
           pushButton_2 calls the openResultsWindow function."""
        super().__init__()
        self.setupUi(self)

        self.VoteScreenButton.clicked.connect(lambda: self.openVoteWindow())
        self.pushButton.clicked.connect(lambda: self.openCandidateWindow())
        self.pushButton_2.clicked.connect(lambda: self.openResultsWindow())

    def openVoteWindow(self) -> None:
        """Hides the main menu and shows the vote screen"""
        self.hide()
        self.voteWindow = VoteLogic(self)
        self.voteWindow.show()

    def openCandidateWindow(self) -> None:
        """Hides the main menu and shows the candidates screen"""
        self.hide()
        self.CandidateWindow = CandidatesLogic(self)
        self.CandidateWindow.show()

    def openResultsWindow(self) -> None:
        """Hides the main menu and shows the results screen"""
        self.hide()
        self.ResultsWindow = ResultsLogic(self)
        self.ResultsWindow.show()
