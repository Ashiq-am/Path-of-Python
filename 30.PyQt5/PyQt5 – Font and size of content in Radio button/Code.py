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
		self.radio_button = QRadioButton("Radio button", self)

		# setting geometry of radio button
		self.radio_button.setGeometry(200, 150, 120, 40)

		# creating push button
		self.button = QPushButton("press to change", self)

		# adding action to push button
		self.button.pressed.connect(self.change)

		# setting geometry to button
		self.button.setGeometry(100, 100, 100, 40)


	# method called by push button
	def change(self):

		# setting font to the style sheet
		self.radio_button.setStyleSheet("QRadioButton"
										"{"
										"font : 20px Arial;"
										"}")

		# adjusting the size
		self.radio_button.adjustSize()



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
