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

		# creating a QDateEdit widget
		date = QDateEdit(self)

		# setting geometry of the date edit
		date.setGeometry(100, 100, 150, 40)

		# creating push button
		push = QPushButton("Select", self)

		# setting geometry to the push button
		push.setGeometry(100, 150, 120, 30)

		# adding action to the push button
		# when it get clicked
		push.clicked.connect(lambda: push_method())

		# method called by push button
		def push_method():

			# selecting text
			date.selectAll()




# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
