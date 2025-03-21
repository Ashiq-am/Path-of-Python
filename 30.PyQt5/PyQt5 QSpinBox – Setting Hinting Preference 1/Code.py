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
		self.spin.setPrefix("PREFIX ")

		# setting suffix to spin
		self.spin.setSuffix(" SUFFIX")

		# getting font of the spin box
		font = self.spin.font()

		# setting hinting preference
		font.setHintingPreference(QFont.PreferFullHinting)

		# reassigning this font to the spin box
		self.spin.setFont(font)

		# creating a label
		label = QLabel(self)

		# setting geometry to the label
		label.setGeometry(100, 200, 300, 60)

		# getting hitting preference
		check = font.hintingPreference()

		# setting text to the label
		label.setText("Hitting Preference : " + str(check))


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
