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
		# to stop the predefined action
		self.calendar.grabKeyboard()


	# overriding key release event
	def keyPressEvent(self, e):


		# creating a key list according to the month
		keylist = [Qt.Key_J, Qt.Key_F, Qt.Key_M, Qt.Key_A, Qt.Key_M, Qt.Key_J,
				Qt.Key_J, Qt.Key_A, Qt.Key_S, Qt.Key_O, Qt.Key_N, Qt.Key_D]

		# getting current month
		month = self.calendar.monthShown()

		# getting current year
		year = self.calendar.yearShown()

		# when J key is pressed
		if e.key() == keylist[0]:
			print("J Key Pressed")

			# if current month is January
			if month == 1:

				# set month as June
				self.calendar.setCurrentPage(year, 6)

			# if current month is June
			elif month == 6:

				# set month as July
				self.calendar.setCurrentPage(year, 7)

			# if current month is not june or july
			else:

				# set month as January
				self.calendar.setCurrentPage(year, 1)

		# if M key is pressed
		elif e.key() == keylist[2]:
			print("M key pressed")

			# if current month is March
			if month == 3:

				# set month as May
				self.calendar.setCurrentPage(year, 5)

			# if current month is not May
			else:
				# set month as March
				self.calendar.setCurrentPage(year, 3)

		# if A key is pressed
		elif e.key() == keylist[3]:
			print("A key pressed")

			# if current month is April
			if month == 4:

				# set month as August
				self.calendar.setCurrentPage(year, 8)

			# if current month is not August
			else:
				# set month as April
				self.calendar.setCurrentPage(year, 4)

		# if any other key is pressed
		elif e.key() in keylist:

			# get the position of the key in the list
			index = keylist.index(e.key())
			print(str(index + 1) + " Month Key Pressed")

			# set the month
			self.calendar.setCurrentPage(year, index + 1 )




# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
