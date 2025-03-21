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
		self.setGeometry(100, 100, 500, 400)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

	# method for components
	def UiComponents(self):

		# creating a QDateEdit widget
		date = QDateEdit(self)

		# setting geometry of the date edit
		date.setGeometry(100, 100, 150, 40)

		# creating a label
		label = QLabel("GeeksforGeeks", self)

		# setting geometry
		label.setGeometry(100, 150, 200, 60)

		# making label multiline
		label.setWordWrap(True)

		# getting name change signal
		date.objectNameChanged.connect(lambda: date_method())

		# method called by date edit
		def date_method():

			# setting text to the label
			label.setText("Name Change Signal Emitted")

		# setting name to the dat edit
		date.setObjectName("Geeks")


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
