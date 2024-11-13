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

		# setting maximum value of progress bar to 200
		bar.setMaximum(200)

		# setting value to progress bar
		bar.setValue(100)

		# getting maximum value of progress bar
		value = bar.maximum()

		# creating label to print the value
		label = QLabel("maximum value = " + str(value), self)

		# adjusting the size of label
		label.adjustSize()

		# moving the label
		label.move(200, 200)

		# setting alignment to centre
		bar.setAlignment(Qt.AlignCenter)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
