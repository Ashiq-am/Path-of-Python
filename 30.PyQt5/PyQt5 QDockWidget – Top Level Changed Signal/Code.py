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

		# creating dock widget
		dock = QDockWidget(self)

		# setting title to the doc widget
		dock.setWindowTitle("GfG Dock")


		# push button
		push = QPushButton("Press", self)

		# setting widget to the dock
		dock.setWidget(push)

		# creating a label
		label = QLabel("GeeksforGeeks", self)

		# setting geometry to the label
		label.setGeometry(100, 200, 300, 80)

		# making label multi line
		label.setWordWrap(True)

		# setting geometry tot he dock widget
		dock.setGeometry(100, 0, 200, 30)

		# getting top level changed changed signal
		# setting text to the label
		dock.topLevelChanged.connect(lambda: label.setText("Top level Changed Signal Emitted"))



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
