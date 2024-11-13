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
        self.setGeometry(100, 100, 500, 400)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for components
    def UiComponents(self):
        # creating a command link button
        cl_button = QCommandLinkButton("Press", self)

        # making it chekable
        cl_button.setCheckable(True)

        # setting geometry
        cl_button.setGeometry(150, 100, 200, 50)

        # setting style sheet
        # setting border to it for checked and unchecked state
        cl_button.setStyleSheet("QCommandLinkButton::checked"
                                "{"
                                "border : 4px solid green;"
                                "}"
                                "QCommandLinkButton::! checked"
                                "{"
                                "border : 4px solid red;"
                                "}")


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
