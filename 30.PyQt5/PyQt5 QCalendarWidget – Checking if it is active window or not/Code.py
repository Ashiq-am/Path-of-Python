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
		self.calender = QCalendarWidget(self)

		# setting geometry to the calender
		self.calender.setGeometry(10, 10, 400, 250)

		# setting name
		self.calender.setAccessibleName("Geek Calendar")

		# making it an active window
		self.calender.activateWindow()


		# creating a label
		label = QLabel(self)

		# setting geometry to the label
		label.setGeometry(100, 280, 250, 60)

		# making label multi line
		label.setWordWrap(True)

		# checking active window
		value = self.calender.isActiveWindow()

		# setting text to the label
		label.setText("Active Window(Checking inside the class) " + str(value))


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# checking if active window
# outside the class
check = window.calender.isActiveWindow()
print("Active window : " + str(check))

# start the app
sys.exit(App.exec())
