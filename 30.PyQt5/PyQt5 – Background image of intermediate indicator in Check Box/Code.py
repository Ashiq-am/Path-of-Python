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
		checkbox.setGeometry(200, 150, 100, 60)

		# setting tristate check box
		checkbox.setTristate(True)

		# changing size of indicator
		# adding background image to the indicator
		# when it is in intermediate state
		checkbox.setStyleSheet("QCheckBox::indicator"
							"{"
							"width : 60px;"
							"height : 60px;"
							"}"
							"QCheckBox::indicator:indeterminate"
							"{"
							"background-image : url(indicator_image.png);"
							"}")


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
