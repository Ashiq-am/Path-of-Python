# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

# custom class for String Spin Box
class StringBox(QSpinBox):

	# constructor
	def __init__(self, parent = None):
		super(StringBox, self).__init__(parent)

		# list of strings
		strings = ["a", "b", "c", "d", "e", "f", "g"]


		# calling set Strings method with
		# adding blank value in front and in end
		self.setStrings(["BLANK"] + strings + ["BLANK"])

		# show first value from index 1
		self.setValue(1)

	def reset_spin(self):
		if self.value() == len(self.strings()) - 1:
			self.setValue(0)

	# method setString
	# similar to set value method
	def setStrings(self, strings):

		# making strings list
		strings = list(strings)

		# making tuple from the string list
		self._strings = tuple(strings)

		# creating a dictionary
		self._values = dict(zip(strings, range(len(strings))))

		# setting range to it the spin box
		self.setRange(0, len(strings)-1)

	# overwriting the textFromValue method
	def textFromValue(self, value):

		# returning string from index
		# _string = tuple
		return self._strings[value]

	# overwriting the stepBy method
	# method that get called when values incremented
	def stepBy(self, step):

		# checking if current value is 1 and step is -1
		# step = -1 means decrement
		if self.value() == 1 and step == -1:

			# set current value to maximum
			self.setValue(self.maximum())

		# checking if current value is maximum -1 and step is 1
		# step = 1 means Increment
		elif self.value() == self.maximum() - 1 and step == 1:

			# setting current value to 0
			self.setValue(0)

		# calling stepBy method by QSpinBox
		QSpinBox.stepBy(self, step)

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

		# creating a string spin box
		string_spin_box = StringBox(self)

		# setting geometry to the spin box
		string_spin_box.setGeometry(100, 100, 200, 40)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
