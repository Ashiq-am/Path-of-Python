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
		bar1 = QProgressBar(self)

		# setting geometry to progress bar
		bar1.setGeometry(200, 100, 200, 30)

		# setting the value
		bar1.setValue(70)

		# getting format of bar1
		format1 = bar1.format()

		# printing the format1
		print("format of bar 1 : " + format1)

		bar2 = QProgressBar(self)

		# setting geometry to progress bar
		bar2.setGeometry(200, 200, 200, 30)

		# setting the value
		bar2.setValue(50)

		# setting text using format
		bar2.setFormat("Geeks")

		# getting format of bar2
		format2 = bar2.format()

		# printing the format2
		print("format of bar 2 : " + format2)


App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
