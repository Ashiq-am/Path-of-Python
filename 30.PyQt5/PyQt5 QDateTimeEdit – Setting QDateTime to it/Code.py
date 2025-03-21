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

		# creating a QDateTimeEdit widget
		datetimeedit = QDateTimeEdit(self)

		# setting geometry
		datetimeedit.setGeometry(100, 100, 150, 35)

		# creating a label
		label = QLabel("GeeksforGeeks", self)

		# setting geometry to the label
		label.setGeometry(100, 160, 200, 60)

		# making label multi line
		label.setWordWrap(True)

		# QDateTime
		dt = QDateTime(2020, 10, 10, 21, 30)

		# setting date time to datetimeedit
		datetimeedit.setDateTime(dt)



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
