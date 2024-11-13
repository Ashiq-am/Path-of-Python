# importing Qt widgets
from PyQt5.QtWidgets import *

# importing system
import sys

# importing numpy as np
import numpy as np

# importing pyqtgraph as pg
import pyqtgraph as pg
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("PyQtGraph")

		# setting geometry
		self.setGeometry(100, 100, 700, 550)

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

		# text
		text = "Data Slicing"

		# creating a label
		label = QLabel(text)

		# setting minimum width
		label.setMinimumWidth(130)

		# making label do word wrap
		label.setWordWrap(True)

		# creating a window for graphs
		win = QMainWindow()

		# creating a widget object
		cwid = QWidget()

		# setting central widget to the graph window
		win.setCentralWidget(cwid)

		# creating a grid layout
		lay = QGridLayout()

		# setitng grid layout to central widget of graphs
		cwid.setLayout(lay)

		# creating a image view objects
		imv1 = pg.ImageView()
		imv2 = pg.ImageView()

		# adding image view objects to the layout
		lay.addWidget(imv1, 0, 0)
		lay.addWidget(imv2, 1, 0)

		# creating a ROI object for selecting slice
		roi = pg.LineSegmentROI([[30, 64], [100, 64]], pen='r')

		# add roi to image view 1
		imv1.addItem(roi)

		# creating 3d data
		# x value using numpy
		x1 = np.linspace(-30, 10, 128)[:, np.newaxis, np.newaxis]
		x2 = np.linspace(-20, 20, 128)[:, np.newaxis, np.newaxis]

		# y value using numpy
		y = np.linspace(-30, 10, 128)[np.newaxis, :, np.newaxis]
		z = np.linspace(-20, 20, 128)[np.newaxis, np.newaxis, :]

		# dimension 1 values
		d1 = np.sqrt(x1 ** 2 + y ** 2 + z ** 2)

		# dimension 2 values
		d2 = 2 * np.sqrt(x1[::-1] ** 2 + y ** 2 + z ** 2)

		# dimension 3 value
		d3 = 4 * np.sqrt(x2 ** 2 + y[:, ::-1] ** 2 + z ** 2)

		# whole data ie all 3 dimensions
		data = (np.sin(d1) / d1 ** 2) + \
			(np.sin(d2) / d2 ** 2) + (np.sin(d3) / d3 ** 2)

		# method to update the image view 2
		def update():

			# get the roi selected data from image view 1
			d2 = roi.getArrayRegion(data, imv1.imageItem, axes=(1, 2))

			# update the image view 2 data
			imv2.setImage(d2)

		# adding update method to the roi
		# when region is changed this method get called
		roi.sigRegionChanged.connect(update)

		# Display the data in both image view
		imv1.setImage(data)

		# setting the range of image view
		imv1.setHistogramRange(-0.01, 0.01)

		# setting levels of the image view
		imv1.setLevels(-0.003, 0.003)

		# call the update method
		update()

		# Creating a grid layout
		layout = QGridLayout()

		# minimum width value of the label
		label.setMinimumWidth(130)

		# setting this layout to the widget
		widget.setLayout(layout)

		# adding label in the layout
		layout.addWidget(label, 1, 0)

		# plot window goes on right side, spanning 3 rows
		layout.addWidget(win, 0, 1, 3, 1)

		# setting this widget as central widget of the main widow
		self.setCentralWidget(widget)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
