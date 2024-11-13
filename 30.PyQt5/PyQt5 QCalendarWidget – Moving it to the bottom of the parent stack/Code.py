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

		# adding color effect to the calendar
		color = QGraphicsColorizeEffect()
		color.setColor(Qt.red)
		self.calendar.setGraphicsEffect(color)

		# creating a another calendar
		another_calendar = QCalendarWidget(self)

		# adjusting the size of another calendar
		another_calendar.adjustSize()

		# lowing the another calendar
		another_calendar.lower()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
