# importing Qt widgets
from PyQt5.QtWidgets import *


import sys

# importing pyqtgraph as pg
import pyqtgraph as pg
from PyQt5.QtGui import *

# Bar Graph class
class BarGraphItem(pg.BarGraphItem):

	# constructor which inherit original
	# BarGraphItem
	def __init__(self, *args, **kwargs):
		pg.BarGraphItem.__init__(self, *args, **kwargs)

	# creating parent changed event
	def mousePressEvent(self, event):

		# rotating the barrgaph
		r = self.rotation()
		self.setRotation(r + 10)

		# print the message
		print("Mouse Press Event")




class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("PyQtGraph")

		# setting geometry
		self.setGeometry(100, 100, 600, 500)


		# icon
		icon = QIcon("skin.png")

		# setting icon to the window
		self.setWindowIcon(icon)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

	# method for components
	def UiComponents(self):

		# creating a widget object
		widget = QWidget()

		# creating a plot window
		plot = pg.plot()

		# create list for y-axis
		y1 = [5, 5, 7, 10, 3, 8, 9, 1, 6, 2]

		# create horizontal list i.e x-axis
		x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

		# create pyqt5graph bar graph item
		# with width = 0.6
		# with bar colors = green
		bargraph = BarGraphItem(x = x, height = y1, width = 0.6, brush ='g')

		# bargraph.viewRangeChanged.connect(lambda: print("sss"))
		# add item to plot window
		# adding bargraph item to the plot window
		plot.addItem(bargraph)

		# Creating a grid layout
		layout = QGridLayout()

		# setting this layout to the widget
		widget.setLayout(layout)

		# plot window goes on right side, spanning 3 rows
		layout.addWidget(plot, 0, 1, 3, 1)

		# setting this widget as central widget of the main widow
		self.setCentralWidget(widget)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
