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

		# creating the check-box
		checkbox = QCheckBox('Geek ?', self)

		# setting geometry of check box
		checkbox.setGeometry(200, 150, 100, 30)

		# getting the caption
		caption = checkbox.text()

		# creating label to print the
		label = QLabel("caption of chheck box = " +
									caption, self)

		# adjusting the size of label
		label.adjustSize()

		# moving the label
		label.move(200, 200)

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
