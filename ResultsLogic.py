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
        with open('results.csv', 'w'):
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

        all_votes = vicVotes + donVotes + nigilVotes
        if all_votes > 0:
            vic_pct = vicVotes / all_votes * 100
            don_pct = donVotes / all_votes * 100
            nigil_pct = nigilVotes / all_votes * 100

            self.don_results_label.setText(f'{donVotes} votes\n{don_pct:.2f}%')
            self.victor_results_label.setText(f'{vicVotes} votes\n{vic_pct:.2f}%')
            self.nigil_results_label.setText(f'{nigilVotes} votes\n{nigil_pct:.2f}%')

        else:
            self.don_results_label.setText(f'0 votes\n0.00%')
            self.victor_results_label.setText(f'0 votes\n0.00%')
            self.nigil_results_label.setText(f'0 votes\n0.00%%')


        if vicVotes > donVotes and vicVotes > nigilVotes:
            self.winner_label.setText(f'The winner is Victor with {vicVotes}\nvotes! Congratulations!')
        elif donVotes > vicVotes and donVotes > nigilVotes:
            self.winner_label.setText(f'The winner is Don with {donVotes}\nvotes! Congratulations!')
        elif nigilVotes > donVotes and nigilVotes > vicVotes:
            self.winner_label.setText(f'The winner is Nigil with {nigilVotes}\nvotes! Congratulations!')
        else:
            self.winner_label.setText(f'Tie! We need more votes.')
