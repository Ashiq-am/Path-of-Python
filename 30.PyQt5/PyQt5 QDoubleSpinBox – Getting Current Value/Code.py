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

		# creating double spin box
		d_spin = QDoubleSpinBox(self)

		# setting geometry to the double spin box
		d_spin.setGeometry(100, 100, 150, 40)

		# value
		value = 9.99

		# setting current value of the double spin box
		d_spin.setValue(value)

		# creating a label
		label = QLabel("GeeksforGeeks", self)

		# setting geometry to the label
		label.setGeometry(100, 200, 300, 80)

		# making label multi line
		label.setWordWrap(True)

		# getting current value of double spin box
		value = d_spin.value()

		# setting text to the label
		label.setText("Current Value : " + str(value))


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
