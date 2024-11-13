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

		# creating a radio button
		self.radio_button = QRadioButton(self)

		# setting geometry of radio button
		self.radio_button.setGeometry(200, 150, 120, 40)

		# setting text to radio button
		self.radio_button.setText("GEEK ?")

		# creating label to display if it is checked or not
		self.label = QLabel("", self)

		# setting geometry of label
		self.label.setGeometry(200, 200, 150, 40)

		# adding action to radio button
		self.radio_button.toggled.connect(self.action)

	# method called by radio button
	def action(self):

		# changing the content of label
		self.label.setText("Action performed")


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
