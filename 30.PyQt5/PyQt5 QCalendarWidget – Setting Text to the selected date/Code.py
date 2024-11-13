# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

# QCalendarWidget Class
class Calendar(QCalendarWidget):

	def paintCell(self, painter, rect, date):
		super(Calendar, self).paintCell(painter, rect, date)

		# checking if date is selected date
		if date == self.selectedDate():

			# saving the painter
			painter.save()

			# creating a QFont object
			font = QFont()

			# setting pixel size of the font
			font.setPixelSize(11)

			# making font bold
			font.setBold(True)

			# making font italic
			font.setItalic(True)

			# setting font to the painter
			painter.setFont(font)

			# drawing text
			painter.drawText(
				rect.topLeft() + QPoint(10, 10),
				"{}".format("Geek"),
			)

			# restoring the painter
			painter.restore()



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

		# creating a QCalendarWidget object
		# as Calendar class inherits QCalendarWidget
		self.calendar = Calendar(self)

		# setting cursor
		self.calendar.setCursor(Qt.PointingHandCursor)

		# setting size of the calendar
		self.calendar.resize(350, 240)

		# setting font to the calendar
		self.calendar.setFont(QFont('Times', 5))

		# move the calendar
		self.calendar.move(10, 10)



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
