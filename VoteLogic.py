from VoteScreen import *
from PyQt6.QtWidgets import *
from mainLogic import *
import csv


class VoteLogic(QMainWindow, Ui_VoteScreen):
    def __init__(self, main_window) -> None:
        """Sets up the gui for the vote screen and gives functionality to the submit and home buttons.
           vote_home_button calls the vote_home function.
           submit_button calls the submit function."""
        super().__init__()
        self.setupUi(self)
        self.vote_home_button.clicked.connect(lambda: self.vote_home())
        self.submit_button.clicked.connect(lambda: self.submit())
        self.main_window = main_window

    def vote_home(self) -> None:
        """Hides the vote screen and shows the main menu"""
        self.hide()
        self.main_window.show()

    def submit(self) -> None:
        """Checks to see which candidate was selected and appends the csv file.
           If the voter selects Don and clicks 'submit', then this function will append 'don I' to the csv
           This also calls the vote_home function. When the submit button is clicked, the user is automatically returned
           to the main menu."""
        with open('results.csv', 'a') as output_file:
            csv_writer = csv.writer(output_file)

            if self.don_vote_button.isChecked():
                csv_writer.writerow(['don', 'I'])
            if self.victor_vote_button.isChecked():
                csv_writer.writerow(['vic', 'I'])
            if self.nigil_vote_button.isChecked():
                csv_writer.writerow(['nigil', 'I'])
        self.vote_home()



