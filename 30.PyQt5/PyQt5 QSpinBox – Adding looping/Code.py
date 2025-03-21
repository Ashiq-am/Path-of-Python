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

		# creating spin box
		self.spin = QSpinBox(self)

		# setting geometry to spin box
		self.spin.setGeometry(100, 100, 150, 40)

		# setting range to the spin box
		self.spin.setRange(-1, 11)

		# setting prefix to spin
		self.spin.setPrefix("Value : ")

		# add action to this spin box
		self.spin.valueChanged.connect(self.action_spin)


	# method called after editing finished
	def action_spin(self):

		# getting current value of spin box
		current = self.spin.value()

		# checking if current value is minimum
		if current == -1:

			# setting spin box value to maximum - 1
			self.spin.setValue(10)

		# checking if current value is maximum
		elif current == 11:

			# setting spin box value to minimum + 1
			self.spin.setValue(0)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
