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
		self.setGeometry(100, 100, 500, 400)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()



	# method for components
	def UiComponents(self):

		# creating a menu bar
		menubar = self.menuBar()

		# creating a selection menu
		selMenu = menubar.addMenu('Selection')

		# creating QAction Instances
		action1 = QAction("One", self)
		action2 = QAction("Two", self)
		action3 = QAction("Three", self)
		action4 = QAction("Four", self)

		# making actions checkable
		action1.setCheckable(True)
		action2.setCheckable(True)
		action3.setCheckable(True)
		action4.setCheckable(True)

		# adding these actions to the selection menu
		selMenu.addAction(action1)
		selMenu.addAction(action2)
		selMenu.addAction(action3)
		selMenu.addAction(action4)

		# creating a action group
		action_group = QActionGroup(self)

		# adding these action to the action group
		action_group.addAction(action1)
		action_group.addAction(action2)
		action_group.addAction(action3)
		action_group.addAction(action4)

		# creating a label
		label = QLabel("GeeksforGeeks", self)

		# setting geometry to the label
		label.setGeometry(100, 150, 200, 50)

		# adding triggered action to the first action
		action1.triggered.connect(lambda: label.setText("Action 1 is Checked"))

		# adding triggered action to the second action
		action2.triggered.connect(lambda: label.setText("Action 2 is Checked"))

		# adding triggered action to the third action
		action3.triggered.connect(lambda: label.setText("Action 3 is Checked"))

		# adding triggered action to the third action
		action4.triggered.connect(lambda: label.setText("Action 4 is Checked"))




# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
