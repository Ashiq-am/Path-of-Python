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
		self.label_1 = QLabel("old label ", self)

		# setting up the border and background color
		self.label_1.setStyleSheet("border :3px solid black background : pink")

		# moving the label
		self.label_1.move(100, 100)

		# creating a new label widget
		self.label_2 = QLabel("new Label ", self)

		# setting up the border and background color
		self.label_2.setStyleSheet("border :3px solid black background : green")

		# setting lower priority to this label
		self.label_2.lower()

		# moving the label
		self.label_2.move(110, 110)


		# show all the widgets
		self.update()
		self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
