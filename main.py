from mainLogic import *
import sys


def main():
    app = QApplication(sys.argv)
    window = mainLogic()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
