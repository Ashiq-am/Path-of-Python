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

		# showing all the widgets
		self.show()

	# method for widgets
	def UiComponents(self):

		# creating a push button
		button1 = QPushButton("First", self)

		# setting geometry of button
		button1.setGeometry(200, 150, 100, 40)

		# adding action to a button
		button1.clicked.connect(self.clickme)

		# creating a push button
		button2 = QPushButton("Second", self)

		# setting geometry of button
		button2.setGeometry(210, 160, 100, 40)

		# adding action to a button
		button2.clicked.connect(self.clickme)

		# make it in lower the window
		button2.lower()


	# action method
	def clickme(self):


		# printing pressed
		print("pressed")

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
