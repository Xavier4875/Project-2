from PyQt6.QtWidgets import *
from ResultsScreen import *
import re
import csv


class ResultsLogic(QMainWindow, Ui_ResultsScreen):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.results_home_button.clicked.connect(lambda: self.results_home())

        self.clear_button.hide()
        self.displayResults()

    def results_home(self):
        with open('results.csv', 'w') as f:
            pass
        self.hide()
        self.main_window.show()

    def displayResults(self):
        """

        :return:
        """
        vicVotes = 0
        nigilVotes = 0
        donVotes = 0
        with open('results.csv', 'r') as input_file:
            for line in input_file:
                if re.match(r'vic', line):
                    vicVotes += 1
                elif re.match(r'don', line):
                    donVotes += 1
                elif re.match(r'nigil', line):
                    nigilVotes += 1
                else:
                    pass
        self.don_results_label.setText(str(donVotes))
        self.victor_results_label.setText(str(vicVotes))
        self.nigil_results_label.setText(str(nigilVotes))

        allVotes = max(vicVotes, donVotes, nigilVotes)

        if vicVotes > donVotes and vicVotes > nigilVotes:
            self.winner_label.setText(f'Winner is Victor with {vicVotes} votes, \n congratulations')
        elif donVotes > vicVotes and donVotes > nigilVotes:
            self.winner_label.setText(f'Winner is Don with {donVotes} votes \n congratulations')
        elif nigilVotes > donVotes and nigilVotes > vicVotes:
            self.winner_label.setText(f'Winner is Nigil with {nigilVotes} votes \n congratulations')
        else:
            self.winner_label.setText(f'Tie needs a second round')
