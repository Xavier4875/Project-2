# Form implementation generated from reading ui file 'DonScreen.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DonScreen(object):
    def setupUi(self, DonScreen):
        DonScreen.setObjectName("DonScreen")
        DonScreen.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(14)
        DonScreen.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=DonScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.don_profile_image = QtWidgets.QLabel(parent=self.centralwidget)
        self.don_profile_image.setGeometry(QtCore.QRect(130, 10, 241, 331))
        self.don_profile_image.setStyleSheet("image: url(:/newPrefix/Don-Beyer.jpg);")
        self.don_profile_image.setText("")
        self.don_profile_image.setPixmap(QtGui.QPixmap("Don-Beyer.jpg"))
        self.don_profile_image.setScaledContents(True)
        self.don_profile_image.setObjectName("don_profile_image")
        self.don_profile_image_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.don_profile_image_label.setGeometry(QtCore.QRect(210, 340, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.don_profile_image_label.setFont(font)
        self.don_profile_image_label.setObjectName("don_profile_image_label")
        self.don_profile_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.don_profile_label.setGeometry(QtCore.QRect(480, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.don_profile_label.setFont(font)
        self.don_profile_label.setObjectName("don_profile_label")
        self.don_profile_label2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.don_profile_label2.setGeometry(QtCore.QRect(430, 50, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.don_profile_label2.setFont(font)
        self.don_profile_label2.setObjectName("don_profile_label2")
        self.don_profile_label3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.don_profile_label3.setGeometry(QtCore.QRect(420, 100, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.don_profile_label3.setFont(font)
        self.don_profile_label3.setObjectName("don_profile_label3")
        self.don_profile_label4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.don_profile_label4.setGeometry(QtCore.QRect(420, 160, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.don_profile_label4.setFont(font)
        self.don_profile_label4.setObjectName("don_profile_label4")
        self.don_profile_label5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.don_profile_label5.setGeometry(QtCore.QRect(390, 230, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.don_profile_label5.setFont(font)
        self.don_profile_label5.setObjectName("don_profile_label5")
        self.don_profile_label6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.don_profile_label6.setGeometry(QtCore.QRect(420, 300, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.don_profile_label6.setFont(font)
        self.don_profile_label6.setObjectName("don_profile_label6")
        self.don_profile_home_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.don_profile_home_button.setGeometry(QtCore.QRect(670, 510, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.don_profile_home_button.setFont(font)
        self.don_profile_home_button.setObjectName("don_profile_home_button")
        DonScreen.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=DonScreen)
        self.statusbar.setObjectName("statusbar")
        DonScreen.setStatusBar(self.statusbar)

        self.retranslateUi(DonScreen)
        QtCore.QMetaObject.connectSlotsByName(DonScreen)

    def retranslateUi(self, DonScreen):
        _translate = QtCore.QCoreApplication.translate
        DonScreen.setWindowTitle(_translate("DonScreen", "MainWindow"))
        self.don_profile_image_label.setText(_translate("DonScreen", "Don Beyer"))
        self.don_profile_label.setText(_translate("DonScreen", "Classical Liberal"))
        self.don_profile_label2.setText(_translate("DonScreen", "Maintain The Status Quo"))
        self.don_profile_label3.setText(_translate("DonScreen", "Intervene In Foreign Wars"))
        self.don_profile_label4.setText(_translate("DonScreen", "Economic War With China \n"
"And Russia"))
        self.don_profile_label5.setText(_translate("DonScreen", "Lower Taxes, Limited Government, \n"
"Individual Liberty"))
        self.don_profile_label6.setText(_translate("DonScreen", "Israel Is Our Greatest Ally "))
        self.don_profile_home_button.setText(_translate("DonScreen", "Candidates"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DonScreen = QtWidgets.QMainWindow()
    ui = Ui_DonScreen()
    ui.setupUi(DonScreen)
    DonScreen.show()
    sys.exit(app.exec())
