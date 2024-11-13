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
		# creating a command link button
		cl_button = QCommandLinkButton("Press", self)

		# setting geometry
		cl_button.setGeometry(150, 100, 150, 60)

		# QActions
		action1 = QAction("Geeks", self)
		action2 = QAction("GfG", self)

		# making action2 checkable
		action2.setCheckable(True)



		# QMenu
		menu = QMenu()

		# adding actions to menu
		menu.addActions([action1, action2])

		# setting menu to the button
		cl_button.setMenu(menu)


		# creating label
		label = QLabel("GeeksforGeeks", self)

		# setting label geometry
		label.setGeometry(100, 200, 300, 80)

		# making label multiline
		label.setWordWrap(True)

		# adding method to the action
		action1.triggered.connect(lambda: label.setText("Action1 is triggered"))

		# adding method to the action2 when it get checked
		action2.toggled.connect(lambda: label.setText("Action2 is toggled"))



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
