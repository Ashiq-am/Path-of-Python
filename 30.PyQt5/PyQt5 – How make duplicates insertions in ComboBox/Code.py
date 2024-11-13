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

		# creating a combo box widget
		self.combo_box = QComboBox(self)

		# setting geometry of combo box
		self.combo_box.setGeometry(200, 150, 120, 30)

		# geek list
		geek_list = ["Geek", "Geeky Geek"]

		# adding list of items to combo box
		self.combo_box.addItems(geek_list)

		# making it editable combo box
		self.combo_box.setEditable(True)

		# allowing duplication of items
		# setting duplicates = True
		self.combo_box.setDuplicatesEnabled(True)



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
