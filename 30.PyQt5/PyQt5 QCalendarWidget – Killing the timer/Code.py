# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


# QCalendarWidget Class
class Calendar(QCalendarWidget):

    # constructor
    def __init__(self, parent=None):
        super(Calendar, self).__init__(parent)

    # overriding the timer event
    # this will show the next month
    def timerEvent(self, event):
        # show the next month
        window.calendar.showNextMonth()


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
        # as Calendar class inherits QCalendarWidget
        self.calendar = Calendar(self)

        # setting geometry to the calender
        self.calendar.setGeometry(50, 10, 400, 250)

        # setting cursor
        self.calendar.setCursor(Qt.PointingHandCursor)

        # starting the calendar timer
        # passing 1000 milliseconds as parameter
        self.timer_id = self.calendar.startTimer(1000)

        # creating a push button
        push = QPushButton("Kill Timer", self)

        # setting geometry to the push button
        push.setGeometry(100, 280, 120, 40)

        # adding action to the push button
        push.clicked.connect(self.do_Action)

    def do_Action(self):
        # killing the timer
        self.calendar.killTimer(self.timer_id)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
