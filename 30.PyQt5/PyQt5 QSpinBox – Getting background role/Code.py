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
		self.spin.setGeometry(100, 100, 250, 40)

		# setting prefix to spin
		self.spin.setPrefix("Prefix ")

		# setting suffix to spin
		self.spin.setSuffix(" Suffix")


		# creating a label
		label = QLabel(self)

		# setting geometry to the label
		label.setGeometry(100, 200, 300, 30)

		# getting the background role object
		object = self.backgroundRole()

		# setting text to the label
		label.setText("Background role object value : " + str(object))


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
