# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# making background color light yellow
		self.setStyleSheet("background : lightyellow;")

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

		# setting geometry to the label
		label.setGeometry(200, 100, 150, 60)

		# setting alignment to the label
		label.setAlignment(Qt.AlignCenter)

		# setting font
		label.setFont(QFont('Arial', 15))

		# creating a color effect
		color_effect = QGraphicsColorizeEffect()

		# setting color to color effect
		color_effect.setColor(Qt.darkRed)

		# setting strength
		color_effect.setStrength(0.5)

		# adding color effect to the label
		label.setGraphicsEffect(color_effect)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
