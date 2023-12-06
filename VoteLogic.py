from VoteScreen import *
from PyQt6.QtWidgets import *
from mainLogic import *
import csv


class VoteLogic(QMainWindow, Ui_VoteScreen):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.vote_home_button.clicked.connect(lambda: self.vote_home())
        self.submit_button.clicked.connect(lambda: self.submit())
        self.main_window = main_window

    def vote_home(self):
        self.hide()
        self.main_window.show()

    def submit(self):
        with open('results.csv', 'a') as output_file:
            csv_writer = csv.writer(output_file)

            if self.don_vote_button.isChecked():
                csv_writer.writerow(['don', 'I'])
            if self.victor_vote_button.isChecked():
                csv_writer.writerow(['vic', 'I'])
            if self.nigil_vote_button.isChecked():
                csv_writer.writerow(['nigil', 'I'])
        self.vote_home()



