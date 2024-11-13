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

		# name
		name = "Geeky"

		# setting up object name
		self.spin.setObjectName(name)

		# adding action when the spin box object name is changed
		self.spin.objectNameChanged.connect(self.spin_method)


		# creating label
		self.label = QLabel(self)

		# setting geometry
		self.label.setGeometry(100, 200, 300, 40)

		# getting object name
		get_name = self.spin.objectName()

		# setting text to the label
		self.label.setText("Object Name : " + get_name)

		# creating a push button
		push = QPushButton("Press", self)

		# adding action to the push button
		push.pressed.connect(self.push_method)

	# method called when object name is changed
	def spin_method(self):
		# setting suffix
		self.spin.setSuffix(" Name changed")

	# method called by push button
	def push_method(self):
		# setting object name of spin box
		self.spin.setObjectName("New")

		# getting object name
		get_name = self.spin.objectName()

		# showing this new name to label
		self.label.setText("Object Name : " + get_name)

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
