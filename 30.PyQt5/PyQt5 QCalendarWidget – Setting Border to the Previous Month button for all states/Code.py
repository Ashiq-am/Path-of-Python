# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

# QCalendarWidget Class
class Calendar(QCalendarWidget):

	# constructor
	def __init__(self, parent = None):
		super(Calendar, self).__init__(parent)



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

		# creating a QCalendarWidget object
		# as Calendar class inherits QCalendarWidget
		self.calendar = Calendar(self)

		# setting cursor
		self.calendar.setCursor(Qt.PointingHandCursor)

		# setting size of the calendar
		self.calendar.resize(350, 240)

		# move the calendar
		self.calendar.move(10, 10)

		# setting stylesheet
		# adding border to the navigation bar previous month button
		# adding border when mouse hover over it and when it get pressed
		self.calendar.setStyleSheet("QCalendarWidget QToolButton# qt_calendar_prevmonth"
									"{"
									"border : 4px solid red;"
									"}"
									"QCalendarWidget QToolButton# qt_calendar_prevmonth::hover"
									"{"
									"border : 4px solid green;"
									"}"
									"QCalendarWidget QToolButton# qt_calendar_prevmonth::pressed"
									"{"
									"border : 4px solid blue;"
									"}"
									)



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
