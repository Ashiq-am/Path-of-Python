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
		self.label_1 = QLabel("Label ", self)

		# setting up the border with different size
		self.label_1.setStyleSheet("border : solid black;"
								"border-width : 10px 1px 10px 1px;")

		# resizing the label
		self.label_1.resize(100, 40)

		# moving the label
		self.label_1.move(100, 100)

		# show all the widgets
		self.update()
		self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
