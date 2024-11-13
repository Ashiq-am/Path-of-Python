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
		# creating label
		label1 = QLabel(self)

		# setting geometry to the label
		label1.setGeometry(200, 150, 100, 50)

		# adding border to the label
		label1.setStyleSheet("border : 2px solid black;")

		# creating label
		label2 = QLabel("Multi label i.e With multi line", self)

		# setting geometry to the label
		label2.setGeometry(200, 250, 100, 50)

		# adding border to the label
		label2.setStyleSheet("border : 2px solid black;")

		# making it multi line
		label2.setWordWrap(True)

		# check
		check = label2.wordWrap()

		# checking if label2 is multi line or not
		if check:
			label1.setText("YESSS")

		else:
			label1.setText("NOO")


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

window.show()

# start the app
sys.exit(App.exec())
