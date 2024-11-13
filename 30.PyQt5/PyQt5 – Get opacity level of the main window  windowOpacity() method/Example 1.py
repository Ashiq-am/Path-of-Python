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

		# getting opacity level
		level = str(self.windowOpacity())

		# creating a label widget
		self.label_1 = QLabel(level, self)

		# moving position
		self.label_1.move(100, 100)

		# setting up the border
		self.label_1.setStyleSheet("border :3px solid blue;")

		# show all the widgets
		self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()
# start the app
sys.exit(App.exec())
