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

		# setting suffix to spin
		self.spin.setSuffix(" Spin Box")

		# creating label
		self.label = QLabel(self)

		# setting geometry
		self.label.setGeometry(100, 200, 300, 40)

		# setting text to the label
		self.label.setText("Spin box will delete when button get pressed")

		# creating a push button
		push = QPushButton("Press", self)

		# adding action to the push button
		push.pressed.connect(self.push_method)

	# method called by push button
	def push_method(self):

		# deleting the spin box
		self.spin.deleteLater()

		# showing this new name to label
		self.label.setText("Spin box is deleted")

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
