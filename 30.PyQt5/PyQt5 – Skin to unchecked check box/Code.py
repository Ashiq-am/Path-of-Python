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
		checkbox1 = QCheckBox('Geek ?', self)

		# setting geometry of check box
		checkbox1.setGeometry(200, 150, 100, 40)

		# setting tri-state check box
		checkbox1.setTristate(True)

		# changing style sheet code of check box
		# adding skin to unchecked check box
		checkbox1.setStyleSheet("QCheckBox::unchecked"
								"{"
								"border-image : url(image.png);"
								"}")


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
