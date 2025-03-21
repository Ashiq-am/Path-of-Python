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
		calender = QCalendarWidget(self)

		# setting geometry to the calender
		calender.setGeometry(10, 10, 400, 250)

		# setting grid
		calender.setGridVisible(True)

		# creating label
		label = QLabel(self)

		# setting geometry to the label
		label.setGeometry(100, 270, 250, 60)

		# making label multi line
		label.setWordWrap(True)

		# checking if the calendar has grid
		check = calender.isGridVisible()

		# setting text to the label
		label.setText("Grid Visible : " + str(check))


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
