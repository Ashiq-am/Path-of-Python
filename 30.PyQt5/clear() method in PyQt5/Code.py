# importing the required libraries
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		# set the title
		self.setWindowTitle("Move")

		# setting the geometry of window
		self.setGeometry(0, 0, 500, 300)

		# creating a label widget
		self.label1 = QLabel('Label 1', self)

		# moving the widget
		# move(left, top)
		self.label1.move(100, 100)

		# creating a label widget
		self.label2 = QLabel('Label 2 ', self)

		# moving the widget
		# move(left, top)
		self.label2.move(100, 120)

		# clearing label 2
		self.label2.clear()

		# creating a label widget
		self.label3 = QLabel('Label 3', self)

		# moving the widget
		# move(left, top)
		self.label3.move(100, 140)



		# show all the widgets
		self.show()

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
