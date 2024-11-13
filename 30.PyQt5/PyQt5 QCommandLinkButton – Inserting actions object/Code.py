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
		cl_button.setGeometry(200, 100, 150, 60)

		# QActions
		a = QAction("Next Geeks", self)
		b = QAction("Previous Geeks", self)


		# QMenu
		menu = QMenu()

		# adding actions to menu
		menu.addActions([a, b])

		# QAction
		c = QAction("Middle", self)

		# inserting action
		menu.insertAction(b, c)

		# setting menu to the button
		cl_button.setMenu(menu)

		# creating QAction object
		q = QAction("Action")

		# action to the button
		cl_button.addAction(q)

		# creating label
		label = QLabel("GeeksforGeeks", self)

		# setting label geometry
		label.setGeometry(50, 200, 300, 80)

		# making label multiline
		label.setWordWrap(True)

		# getting action list
		value = cl_button.actions()

		# setting text to the label
		label.setText("Actions List : " + str(value))





# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
