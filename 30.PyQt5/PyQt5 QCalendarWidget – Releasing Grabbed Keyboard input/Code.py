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

		# grabbing keyboard input
		self.calendar.grabKeyboard()

		# creating a push button
		push = QPushButton("Release Keyboard", self)

		# setting geometry tot he push button
		push.setGeometry(100, 280, 150, 40)

		# adding action to the push button
		push.clicked.connect(self.do_action)

	def do_action(self):

		# releasing the keyboard
		self.calendar.releaseKeyboard()

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
