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

		# setting range to the spin box
		self.spin.setRange(0, 999999)

		# setting prefix to spin
		self.spin.setPrefix("Prefix ")

		# setting suffix to spin
		self.spin.setSuffix(" Suffix")

		# adding property to the spin box
		self.spin.setProperty("Dynamic", 1)

		# adding property to the spin box
		self.spin.setProperty("Has suffix", 1)

		# creating label
		self.label = QLabel(self)

		# setting geometry to the label
		self.label.setGeometry(100, 200, 300, 70)

		# making it multi line label
		self.label.setWordWrap(True)

		# getting property names
		p_names = self.spin.dynamicPropertyNames()

		# setting text to the label
		self.label.setText(str(p_names))

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()
window.spin.setFocus()
# start the app
sys.exit(App.exec())
