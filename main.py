from mainLogic import *
import sys


def main():
    """Opens the main menu"""
    app = QApplication(sys.argv)
    window = MainLogic()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
