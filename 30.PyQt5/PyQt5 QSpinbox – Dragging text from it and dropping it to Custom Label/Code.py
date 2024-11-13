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


		# get the line edit object
		line = self.spin.lineEdit()

		# set drag enable to true
		line.setDragEnabled(True)

		# creating a CustomLabel object
		label = CustomLabel('Drop here.', self)

		# setting geometry to the label
		label.setGeometry(100, 200, 300, 30)


class CustomLabel(QLabel):
	# constructor
	def __init__(self, title, parent):
		super().__init__(title, parent)

		# enabling accept drops
		self.setAcceptDrops(True)

	# creating drag enter event to receive text
	def dragEnterEvent(self, e):

		# checking format of the text
		if e.mimeData().hasFormat('text / plain'):
			# accepting the text
			e.accept()

		else:
			# rejecting the text
			e.ignore()

	# drop event to showing the text to label
	def dropEvent(self, e):

		# setting text to the label
		self.setText(e.mimeData().text())


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
