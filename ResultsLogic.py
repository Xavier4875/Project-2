from PyQt6.QtWidgets import *
from ResultsScreen import *
import re
import csv


class ResultsLogic(QMainWindow, Ui_ResultsScreen):
    def __init__(self, main_window):
        """Sets up the gui for the results screen and gives functionality to the home button.
           results_home_button calls the results_home function
           This function also calls displayResults() so the results are displayed automatically."""
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.results_home_button.clicked.connect(lambda: self.results_home())
        self.displayResults()

    def results_home(self) -> None:
        """Hides the results screen and shows the main menu
           This function also clears out results.csv; Each time the home button is clicked, the votes are erased."""
        with open('results.csv', 'w') as f:
            pass
        self.hide()
        self.main_window.show()

    def displayResults(self):
        """This function displays the results. Variables are created to keep track of each candidate's vote tally."""
        vicVotes = 0
        nigilVotes = 0
        donVotes = 0
        with open('results.csv', 'r') as input_file:
            """Reads the csv file and adds one to each candidates variable every time their name is found."""
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
            self.don_results_label.setText('0 votes\n0.00%')
            self.victor_results_label.setText('0 votes\n0.00%')
            self.nigil_results_label.setText(f'0 votes\n0.00%')
        """This if-else branch displays each candidate's vote total and the percentage of the 
           total number of votes they received."""

        if vicVotes > donVotes and vicVotes > nigilVotes:
            self.winner_label.setText(f'The winner is Victor with {vicVotes}\nvotes! Congratulations!')
        elif donVotes > vicVotes and donVotes > nigilVotes:
            self.winner_label.setText(f'The winner is Don with {donVotes}\nvotes! Congratulations')
        elif nigilVotes > donVotes and nigilVotes > vicVotes:
            self.winner_label.setText(f'The winner is Nigil with {nigilVotes}\nvotes! Congratulations!')
        else:
            self.winner_label.setText(f'Tie! We need another\nround.')
        """This if-else branch compares the number of votes each candidate received and determines who had the most.
           The name of the winner is displayed as well the number of votes they received.
           If there is a tie, the user will be prompted for another round."""
