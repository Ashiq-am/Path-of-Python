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
		self.setGeometry(100, 100, 650, 400)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

	# method for components
	def UiComponents(self):

		# creating a QCalendarWidget object
		self.calendar = QCalendarWidget(self)

		# setting geometry to the calender
		self.calendar.setGeometry(50, 10, 400, 300)

		# setting cursor
		self.calendar.setCursor(Qt.PointingHandCursor)

		# getting the current lay out
		layout = self.calendar.layout()

		# creating a label
		label = QLabel("GeeksforGeeks", self)

		# setting alignment
		label.setAlignment(Qt.AlignCenter)

		# setting style sheet to the label
		label.setStyleSheet("QLabel"
							"{"
							"border : 1px solid darkgrey;"
							"background : lightgrey;"
							"}")

		# adding label to the layout
		layout.addWidget(label)

		# setting layout back to calendar
		self.calendar.setLayout(layout)




# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
