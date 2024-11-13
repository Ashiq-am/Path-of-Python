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

		# setting the geometry of window
		self.setGeometry(60, 60, 600, 400)


		# creating a label widget
		self.label_1 = QLabel("Normal border", self)

		# moving position
		self.label_1.move(100, 100)

		# setting up the border and padding
		self.label_1.setStyleSheet("border :3px solid black;")

		# resizing label
		self.label_1.resize(100, 80)

		# creating a label widget
		self.label_2 = QLabel("Dashed border", self)

		# setting up the dashed border
		self.label_2.setStyleSheet("border :3px solid black border-style : dashed")

		# moving position
		self.label_2.move(230, 200)

		# resizing the label
		self.label_2.resize(100, 80)

		# show all the widgets
		self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()
# start the app
sys.exit(App.exec())
