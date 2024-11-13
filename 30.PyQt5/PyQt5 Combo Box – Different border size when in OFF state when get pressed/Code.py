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
		# creating a check-able combo box object
		self.combo_box = QComboBox(self)

		# setting geometry of combo box
		self.combo_box.setGeometry(200, 150, 150, 80)

		# geek list
		geek_list = ["Sayian", "Super Sayian", "Super Sayian 2", "Super Sayian B"]

		# adding list of items to combo box
		self.combo_box.addItems(geek_list)

		# setting style sheet
		# adding border to combo box
		# adding different width border when it is OFF and it get pressed
		self.combo_box.setStyleSheet("QComboBox"
									"{"
									"border : 5px solid black;"
									"}"
									"QComboBox::! on:pressed"
									"{"
									"border : solid black;"
									"border-width : 1px 5px 2px 10px;;"									
									"}")


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

window.show()

# start the app
sys.exit(App.exec())
