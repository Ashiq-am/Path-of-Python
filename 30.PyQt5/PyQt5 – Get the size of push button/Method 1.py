# importing libraries
from PyQt5.QtWidgets import *
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



	# method for widgets
	def UiComponents(self):

		# creating a push button
		button = QPushButton("CLICK", self)

		# setting geometry of button
		# rectangular shape i.e width > height
		button.setGeometry(200, 150, 150, 40)

		# adding action to a button
		button.clicked.connect(self.clickme)

		# printing button size
		print(button.size())



	# action method
	def clickme(self):

		# printing pressed
		print("pressed")

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()
