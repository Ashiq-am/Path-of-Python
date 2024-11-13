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
		radio_button = QRadioButton(self)

		# setting geometry of radio button
		radio_button.setGeometry(200, 150, 120, 40)

		# setting text to radio button
		radio_button.setText("GEEK ?")

		# setting the style sheet
		# adding background image to the indicator of radio button
		radio_button.setStyleSheet("QRadioButton::indicator"
								"{"
								"background-image : url(image.png);"
								"}")

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
