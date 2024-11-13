# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# setting background color of window
		# self.setStyleSheet("background-color : black;")

		# setting title
		self.setWindowTitle("Python ")

		# setting geometry
		self.setGeometry(100, 100, 600, 400)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

	# method for widgets
	def UiComponents(self):

		# creating label
		label = QLabel("Label", self)

		# setting alignment
		label.setAlignment(Qt.AlignCenter)

		# setting geometry to the label
		label.setGeometry(200, 100, 150, 60)

		# setting border
		label.setStyleSheet("border : 8px solid black")

		# creating a QGraphicsDropShadowEffect object
		shadow = QGraphicsDropShadowEffect()

		# setting blur radius
		shadow.setBlurRadius(20)

		# setting Yoffset
		shadow.setYOffset(100)

		# adding shadow to the label
		label.setGraphicsEffect(shadow)

		# creating label
		result = QLabel(self)

		# setting geometry
		result.setGeometry(100, 200, 350, 30)

		# getting shadow Y-offset
		Yoffset = shadow.yOffset()

		# showing text through label
		result.setText("Y-Offset : " + str(Yoffset))



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
