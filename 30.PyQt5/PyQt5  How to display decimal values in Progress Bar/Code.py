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

		# creating progress bar
		bar = QProgressBar(self)

		# setting geometry to progress bar
		bar.setGeometry(200, 150, 200, 30)

		# setting value of n for 2 decimal values
		n = 100

		# setting maximum value for 2 decimal points
		bar.setMaximum(100 * n)

		# value in percentage
		value = 75.55

		# setting the value by multiplying it to 100
		bar.setValue(value * n)

		# displaying the decimal value
		bar.setFormat("%.02f %%" % value)

		# setting alignment to centre
		bar.setAlignment(Qt.AlignCenter)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
