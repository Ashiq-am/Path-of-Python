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

		# creating a radio button
		radio_button = QRadioButton(self)

		# setting geometry of radio button
		radio_button.setGeometry(200, 150, 120, 40)

		# setting text to radio button
		radio_button.setText("Radio Button")

		# setting direction
		radio_button.setLayoutDirection(Qt.RightToLeft)

		# creating label to show output
		label = QLabel(self)

		# changing position of label
		label.move(200, 200)

		# check if direction is right to left
		check = radio_button.isRightToLeft()

		# setting output text to label
		label.setText(" Is direction is right to left :" + str(check))

		# adjusting the size of label
		label.adjustSize()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
