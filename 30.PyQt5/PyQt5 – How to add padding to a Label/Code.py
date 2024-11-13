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
		self.label_1 = QLabel("===============", self)

		# moving position
		self.label_1.move(100, 100)

		# setting up the border
		self.label_1.setStyleSheet("border :3px solid blue;")

		# resizing label
		self.label_1.resize(100, 100)
		# creating a label widget
		self.label_2 = QLabel("==================", self)

		# setting up the border and adding padding
		self.label_2.setStyleSheet("border :3px solid blue;padding :15px")

		# moving position
		self.label_2.move(230, 200)

		# resizing the label
		self.label_2.resize(100, 100)

		# show all the widgets
		self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()
# start the app
sys.exit(App.exec())
