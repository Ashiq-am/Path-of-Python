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
		self.statusBar().showMessage("This is status bar")

		# setting border and padding with different sizes
		self.statusBar().setStyleSheet("border :3px solid black;")

		# creating a label widget
		self.label_1 = QLabel("Label 1")


		# setting up the border
		self.label_1.setStyleSheet("border :2px solid blue;")

		# adding label to status bar
		self.statusBar().addPermanentWidget(self.label_1)
		# show all the widgets
		self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()


# start the app
sys.exit(App.exec())
