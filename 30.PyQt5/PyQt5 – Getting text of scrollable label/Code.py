# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


# class for scrollable label
class ScrollLabel(QScrollArea):

	# constructor
	def __init__(self, *args, **kwargs):
		QScrollArea.__init__(self, *args, **kwargs)

		# making widget resizable
		self.setWidgetResizable(True)

		# making qwidget object
		content = QWidget(self)
		self.setWidget(content)

		# vertical box layout
		lay = QVBoxLayout(content)

		# creating label
		self.label = QLabel(content)

		# setting alignment to the text
		self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

		# making label multi-line
		self.label.setWordWrap(True)

		# adding label to the layout
		lay.addWidget(self.label)

	# the setText method
	def setText(self, text):
		# setting text to the label
		self.label.setText(text)

	# getting text method
	def text(self):

		# getting text of the label
		get_text = self.label.text()

		# return the text
		return get_text

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
		# text to show in label
		text = "There are so many options provided by Python to develop GUI "

		# creating scroll label
		label = ScrollLabel(self)

		# setting text to the label
		label.setText(text)

		# setting geometry
		label.setGeometry(10, 100, 100, 80)

		get_text = label.text()

		# creating another label to show the text
		result = QLabel(get_text, self)

		# setting geometry to the label
		result.setGeometry(150, 100, 400, 40)



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

window.show()

# start the app
sys.exit(App.exec())
