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

		# setting status bar message
		self.statusBar().showMessage("This is status bar with different border colors")

		# setting border color for different edge to status bar
		self.statusBar().setStyleSheet("border :5px solid ;"
									"border-top-color : pink; "
									"border-left-color :green;"
									"border-right-color :blue;"
									"border-bottom-color : yellow")


		# creating a label widget
		self.label_1 = QLabel("Status bar", self)

		# moving position
		self.label_1.move(100, 100)

		# setting up the border
		self.label_1.setStyleSheet("border :1px solid blue;")

		# resizing label
		self.label_1.adjustSize()

		# show all the widgets
		self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
