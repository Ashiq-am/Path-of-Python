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

		# creating a QDateTimeEdit widget
		datetimeedit = QDateTimeEdit(self)

		# setting geometry
		datetimeedit.setGeometry(100, 100, 150, 35)

		# creating a push button
		push = QPushButton("Press", self)

		# setting geometry to the push button
		push.setGeometry(120, 160, 120, 35)

		# when push button get clicked connect to the method
		push.clicked.connect(lambda: push_method())

		def push_method():

			# set the selected section
			datetimeedit.setSelectedSection(QDateTimeEdit.MonthSection)




# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
