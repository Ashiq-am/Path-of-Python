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

	# method for widgets
	def UiComponents(self):
		# creating a check-able combo box object
		self.combo_box = QComboBox(self)

		# setting geometry of combo box
		self.combo_box.setGeometry(200, 150, 100, 30)

		# geek list
		geek_list = ["Sayian", "Super Sayian", "Super Sayian 2", "Super Sayian B"]

		# adding list of items to combo box
		self.combo_box.addItems(geek_list)

		# setting stylesheet of the combo box
		self.combo_box.setStyleSheet("border : 1px solid red;")

		# creating a timer object
		timer = QTimer(self)

		# adding action to the timer
		timer.timeout.connect(self.do_something)

		# starting timer
		timer.start(100)

	# action called by the timer
	def do_something(self):

		# checking is mouse is on combo box
		if self.combo_box.underMouse():
			# making size larger
			self.combo_box.resize(110, 40)

		else:
			# making size smaller
			self.combo_box.resize(100, 30)

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
