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


		# creating a command link button
		cl_button = QCommandLinkButton("Press", self)

		# setting geometry
		cl_button.setGeometry(250, 100, 150, 50)

		# making it checkable
		cl_button.setCheckable(True)

		# setting auto default property
		cl_button.setAutoDefault(True)

		# size
		size = QSize(30, 30)

		# setting icon size
		cl_button.setIconSize(size)

		# creating label
		label = QLabel("GeeksforGeeks", self)

		# setting label geometry
		label.setGeometry(50, 100, 200, 40)

		# making label multiline
		label.setWordWrap(True)

		# getting auto default property
		value = cl_button.autoDefault()

		# setting text to the label
		label.setText("Auto Default : " + str(value))




# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
