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

	# method for components
	def UiComponents(self):

		# creating a QCalendarWidget object
		calender = QCalendarWidget(self)

		# setting geometry to the calender
		calender.setGeometry(50, 50, 400, 250)

		# creating a label
		label = QLabel(self)

		# setting geometry to the label
		label.setGeometry(100, 280, 250, 60)

		# making label multi line
		label.setWordWrap(True)

		# text
		text = "Destroyed Signal Emitted "

		# getting the destroyed signal and
		# when receives the signal printing the message
		calender.destroyed.connect(lambda: label.setText(text))

		# creating push button
		push = QPushButton("Destroy ", self)

		# adding action to it
		push.clicked.connect(lambda: calender.deleteLater())





# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
