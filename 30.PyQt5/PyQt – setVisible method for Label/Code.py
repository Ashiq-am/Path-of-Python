# importing the required libraries

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class Window(QMainWindow):
	def __init__(self):
		super().__init__()


		# set the title
		self.setWindowTitle("Python")

		# setting geometry
		self.setGeometry(100, 100, 600, 400)
		# creating a label widget
		self.label_1 = QLabel("Label", self)

		# moving position
		self.label_1.move(0, 0)

		# setting up the border
		self.label_1.setStyleSheet("border :3px solid black;")

		# setting visibility status
		self.label_1.setVisible(False)

		# creating a label widget
		self.label_2 = QLabel("Above there a Label", self)

		# moving position
		self.label_2.move(0, 50)

		# adjust size
		self.label_2.adjustSize()

		# show all the widgets
		self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
