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
		self.color_effect = QGraphicsColorizeEffect()

		# setting color to color effect
		self.color_effect.setColor(Qt.darkBlue)

		# adding color effect to the label
		label.setGraphicsEffect(self.color_effect)

		# creating a radio button
		self.button = QRadioButton("Disable color filter", self)

		# setting geometry
		self.button.setGeometry(200, 200, 300, 30)

		# adding action to the button
		self.button.clicked.connect(self.do_something)

	# action called by the radio button
	def do_something(self):
		# radio is checked ?
		if self.button.isChecked() == True:
			# making color effect disable
			self.color_effect.setEnabled(False)

		else:
			# making color color effect enable
			self.color_effect.setEnabled(True)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
