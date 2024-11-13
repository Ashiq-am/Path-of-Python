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
		self.spin.setGeometry(100, 100, 100, 40)

		# setting display integer base
		self.spin.setDisplayIntegerBase(2)

		# creating label show result
		self.label = QLabel(self)

		# setting geometry
		self.label.setGeometry(100, 200, 200, 40)

		# getting display integer base
		base = self.spin.displayIntegerBase()

		# setting text to the label
		self.label.setText("Base : " + str(base))


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

window.show()

# start the app
sys.exit(App.exec())
