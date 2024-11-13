# importing the required libraries

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
import sys



class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		# set the title
		self.setWindowTitle("Description")

		# setting the geometry of window
		self.setGeometry(0, 0, 400, 300)

		# creating a label widget
		self.label_1 = QLabel("Label", self)

		# moving position
		self.label_1.move(100, 100)

		# setting up border
		self.label_1.setStyleSheet("border: 1px solid black;")

		# setting up the description of label_1
		self.label_1.setAccessibleDescription(
					"This is description of label")

		# getting description of label_1
		info = self.label_1.accessibleDescription()

		# new label to display info
		self.label_2 = QLabel(info, self)
		self.label_2.move(100, 130)
		self.label_2.adjustSize()

		# show all the widgets
		self.show()



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
