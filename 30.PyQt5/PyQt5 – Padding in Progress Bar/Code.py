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
		# creating progress bar
		bar = QProgressBar(self)

		# setting geometry to progress bar
		bar.setGeometry(200, 150, 200, 30)

		# set value to progress bar
		bar.setValue(70)

		# setting alignment to center
		bar.setAlignment(Qt.AlignCenter)

		# setting padding size
		# and border to progress bar
		bar.setStyleSheet("QProgressBar"
						"{"
						"border : 1px solid black;"
						"padding : 5px;"
						"}")


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
