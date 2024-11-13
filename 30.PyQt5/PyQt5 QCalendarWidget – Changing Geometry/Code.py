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
        self.setGeometry(100, 100, 650, 400)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for components
    def UiComponents(self):
        # creating a QCalendarWidget object
        self.calender = QCalendarWidget(self)

        # setting cursor
        self.calender.setCursor(Qt.PointingHandCursor)

        # creating a push button add action
        push = QPushButton("Set Geometry", self)

        # move the push button
        push.move(100, 280)

        # adding action to the push
        push.clicked.connect(self.push_action)

    def push_action(self):
        # setting geometry of the calendar
        self.calender.setGeometry(50, 10, 400, 250)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
