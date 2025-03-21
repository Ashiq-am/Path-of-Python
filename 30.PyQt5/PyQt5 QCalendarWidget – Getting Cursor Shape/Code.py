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

		# setting geometry to the calender
		self.calender.setGeometry(50, 10, 400, 250)

		# setting cursor
		self.calender.setCursor(Qt.PointingHandCursor)

		# creating a label
		label = QLabel(self)

		# setting geometry
		label.setGeometry(50, 280, 420, 120)

		# making it multi line
		label.setWordWrap(True)

		# getting cursor
		value = self.calender.cursor()

		# setting text to the label
		label.setText("Cursor : " + str(value))


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()


# start the app
sys.exit(App.exec())
