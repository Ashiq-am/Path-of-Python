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
		bar.setGeometry(150, 150, 200, 30)

		# set value to progress bar
		bar.setValue(40)

		# setting alignment to center
		bar.setAlignment(Qt.AlignCenter)

		# setting text visibility to false
		bar.setTextVisible(False)

		# getting the visibility status
		visible = bar.isTextVisible()

		# creating label to print visibility status
		label = QLabel("Text visibility status = " + str(visible), self)

		# adjusting the size of label
		label.adjustSize()

		# moving the label
		label.move(160, 200)

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
