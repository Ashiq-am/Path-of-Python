# importing libraries
from PyQt5.QtWidgets import *
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

		# creating a push button
		button = QPushButton("CLICK", self)

		# setting geometry of button
		button.setGeometry(200, 150, 100, 30)

		# adding action to a button
		button.clicked.connect(self.clickme)

		# setting the description
		button.setAccessibleDescription("this is details of button")

		# accessing the description
		info = button.accessibleDescription()

		# creating label to display info
		label = QLabel(info, self)
		# moving the label
		label.move(200, 200)
		# adjusting the size of label
		label.adjustSize()


	# action method
	def clickme(self):

		# printing pressed
		print("pressed")

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
