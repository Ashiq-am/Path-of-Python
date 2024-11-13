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

	# method for components
	def UiComponents(self):

		# creating a QCalendarWidget object
		self.calendar = QCalendarWidget(self)

		# setting geometry to the calender
		self.calendar.setGeometry(50, 50, 400, 250)

		# creating a radio button
		self.radio_button = QRadioButton("Hide", self)

		# setting geometry to the radio button
		self.radio_button.setGeometry(100, 10, 200, 40)

		# adding action to the radio button
		self.radio_button.clicked.connect(self.do_action)


	# action called by the radio button
	def do_action(self):

		# checking state of the radio button
		if self.radio_button.isChecked():

			# hiding the calendar
			self.calendar.hide()

		else:
			self.calendar.show()



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
