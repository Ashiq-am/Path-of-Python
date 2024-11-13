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

		# creating a combo box object
		self.combo_box = QComboBox(self)

		# setting geometry of combo box
		self.combo_box.setGeometry(200, 150, 150, 30)

		# geek list
		geek_list = ["Sayian", "Super Sayian", "Super Sayian 2", "Super Sayian B"]

		# adding list of items to combo box
		self.combo_box.addItems(geek_list)

		# setting tool tip to each item
		self.combo_box.setItemData(0, "This is a tooltip for item[0]", QtCore.Qt.ToolTipRole)
		self.combo_box.setItemData(1, "This is a tooltip for item[1]", QtCore.Qt.ToolTipRole)
		self.combo_box.setItemData(2, "This is a tooltip for item[2]", QtCore.Qt.ToolTipRole)
		self.combo_box.setItemData(3, "This is a tooltip for item[3]", QtCore.Qt.ToolTipRole)



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

window.show()

# start the app
sys.exit(App.exec())
