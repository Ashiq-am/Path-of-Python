# importing the required libraries

from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
import sys

class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		# set the title
		self.setWindowTitle("Label")

		# setting the geometry of window
		self.setGeometry(0, 0, 400, 300)

		# creating a label widget
		# by default label will display at top left corner
		self.label = QLabel('This is label', self)

		# show all the widgets
		self.show()

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
