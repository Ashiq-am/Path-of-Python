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
		self.setGeometry(100, 100, 500, 400)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()


	# method for components
	def UiComponents(self):

		# creating a QColorDialog object
		dialog = QColorDialog(self)

		# executing the dialog
		dialog.exec_()


		# creating label to display the color
		label = QLabel("GfG", self)

		# setting geometry to the label
		label.setGeometry(100, 100, 200, 60)

		# making label multi line
		label.setWordWrap(True)

		# setting stylesheet of the label
		label.setStyleSheet("QLabel"
							"{"
							"border : 5px solid black;"
							"}")

		color = Qt.green

		# setting graphic effect to the label
		graphic = QGraphicsColorizeEffect(self)

		# setting color to the graphic
		graphic.setColor(color)

		# setting graphic to the label
		label.setGraphicsEffect(graphic)



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
