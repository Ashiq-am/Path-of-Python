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
		self.calendar = QCalendarWidget(self)

		# setting geometry to the calender
		self.calendar.setGeometry(50, 10, 400, 250)

		# setting cursor
		self.calendar.setCursor(Qt.PointingHandCursor)

		# grabbing the keyboard for the calendar
		self.calendar.grabKeyboard()

		# creating label to show the properties
		self.label = QLabel(self)

		# setting geometry to the label
		self.label.setGeometry(100, 280, 250, 60)

		# making label multi line
		self.label.setWordWrap(True)

		# getting mouse grabber property
		value = self.calendar.mouseGrabber()

		# setting text to the label
		self.label.setText("Calendar Mouse grabber : " + str(value))



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
