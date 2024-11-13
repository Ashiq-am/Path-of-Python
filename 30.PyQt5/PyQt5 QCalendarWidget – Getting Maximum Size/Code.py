# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

# QCalendarWidget Class
class Calendar(QCalendarWidget):

	# constructor
	def __init__(self, parent = None):
		super(Calendar, self).__init__(parent)
		self.setMouseTracking(True)


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

		# creating a layout
		layout = QVBoxLayout()

		# creating a QCalendarWidget object
		# as Calendar class inherits QCalendarWidget
		self.calendar = Calendar(self)

		# setting cursor
		self.calendar.setCursor(Qt.PointingHandCursor)

		# adding calendar tot he layout
		layout.addWidget(self.calendar)

		# setting maximum size
		self.calendar.setMaximumSize(QSize(500, 400))

		# creating a label
		label = QLabel(self)

		# adding label to the layout
		layout.addWidget(label)

		# getting maximum size
		value = self.calendar.maximumSize()

		# setting text to the label
		label.setText("Maximum Size : " + str(value))

		# setting layout
		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)




# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
