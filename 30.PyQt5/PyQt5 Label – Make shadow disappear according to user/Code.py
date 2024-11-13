# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

	def __init__(self):
		super().__init__()

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
		self.shadow = QGraphicsDropShadowEffect()

		# setting blur radius
		self.shadow.setBlurRadius(30)

		# setting Xoffset
		self.shadow.setOffset(10)

		# adding shadow to the label
		label.setGraphicsEffect(self.shadow)

		# creating radio button
		self.button = QRadioButton("Hide Shadow", self)

		# setting geometry to the radio button
		self.button.setGeometry(200, 200, 100, 40)

		# adding action to the button
		self.button.clicked.connect(self.hide_shadow)

	def hide_shadow(self):

		if self.button.isChecked():

			# making shadow off
			self.shadow.setEnabled(False)

		else:
			# making shadow off
			self.shadow.setEnabled(True)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
