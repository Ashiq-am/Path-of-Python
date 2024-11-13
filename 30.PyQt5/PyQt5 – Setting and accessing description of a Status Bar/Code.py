from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		# set the title
		self.setWindowTitle("Python")

		# setting the geometry of window
		self.setGeometry(60, 60, 600, 400)

		# setting status bar message
		self.statusBar().showMessage("This is status bar ")

		# setting border to status bar
		self.statusBar().setStyleSheet("border :3px solid black;")

		# setting description to status bar
		self.statusBar().setAccessibleDescription(
				"this is description of status bar")


		# creating a label widget to show deciption
		self.label_1 = QLabel( self)

		# moving position
		self.label_1.move(100, 100)

		# setting up the border
		self.label_1.setStyleSheet("border :1px solid blue;")

		# accessing the description
		data = self.statusBar().accessibleDescription()

		# setting text to label
		self.label_1.setText(data)

		# resizing label
		self.label_1.adjustSize()

		# show all the widgets
		self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
