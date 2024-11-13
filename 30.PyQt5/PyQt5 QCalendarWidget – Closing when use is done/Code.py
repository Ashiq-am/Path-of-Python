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
		self.calender = QCalendarWidget(self)

		# setting geometry to the calender
		self.calender.setGeometry(10, 10, 400, 250)

		# creating a push button
		button = QPushButton("Close", self)

		# setting geometry tot he button
		button.setGeometry(100, 280, 100, 40)

		# adding action to the button
		button.clicked.connect(self.do_action)

	# method called by push button
	def do_action(self):

		# closing the calender
		self.calender.close()



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
