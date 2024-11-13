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
		self.spin.setRange(1, 999999)

		# setting prefix to spin
		self.spin.setPrefix("PREFIX ")

		# setting suffix to spin
		self.spin.setSuffix(" SUFFIX")

		# setting under line to the font
		font = self.spin.font()
		font.setUnderline(True)
		self.spin.setFont(font)

		# creating a label
		label = QLabel(self)

		# making label multi line
		label.setWordWrap(True)

		# setting geometry to the label
		label.setGeometry(100, 200, 300, 60)

		# getting the frame size
		f_size = self.spin.frameSize()

		# setting text to the label
		label.setText(str(f_size))


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
