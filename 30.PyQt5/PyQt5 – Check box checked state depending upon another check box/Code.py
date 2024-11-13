# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 600, 400)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):

        # creating the check-box
        self.checkbox1 = QCheckBox('Geek ?', self)

        # setting geometry of check box
        self.checkbox1.setGeometry(200, 150, 100, 40)

        # adding action to check box
        self.checkbox1.stateChanged.connect(self.allow)

        # creating the check-box
        self.checkbox2 = QCheckBox('Geeky Geek ?', self)

        # setting geometry of check box
        self.checkbox2.setGeometry(200, 180, 100, 40)

        # stooping check box to get checked
        self.checkbox2.setCheckable(False)

    # method called by checkbox1
    def allow(self):

        # checking if checkbox1 is checked ?
        if self.checkbox1.isChecked():

            # allow second check box to get checked
            self.checkbox2.setCheckable(True)

        # first check box is unchecked
        else:

            # make second check box unchecked
            self.checkbox2.setCheckState(0)

            # make second check box uncheckable
            self.checkbox2.setCheckable(False)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
