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

		# creating label to show label
		self.label = QLabel(self)

		# setting geometry to the label
		self.label.setGeometry(200, 200, 200, 30)

		# creating a timer object
		timer = QTimer(self)

		# adding action to the timer
		timer.timeout.connect(self.do_something)

		# starting timer
		timer.start(100)

	# action called by the timer
	def do_something(self):

		# checking if the combo box is under mouse
		under = self.combo_box.underMouse()

		# setting text to the label
		self.label.setText("Under Mouse ? : " + str(under))

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
