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
		label = QLabel("Hello Geeks", self)

		# setting geometry of the label
		label.setGeometry(200, 150, 100, 40)

		# setting background color to label when
		# mouse is not hovering over it(anti hover)
		label.setStyleSheet("QLabel::! hover"
							"{"
							"background-color : lightgreen;"
							"}")


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
