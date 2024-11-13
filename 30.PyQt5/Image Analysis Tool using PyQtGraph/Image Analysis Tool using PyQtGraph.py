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
		self.setGeometry(100, 100, 900, 550)

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
		text = "Image Analysis"

		# creating a label
		label = QLabel(text)

		# setting minimum width
		label.setMinimumWidth(130)

		# making label do word wrap
		label.setWordWrap(True)

		# creating a graphic layout widget

		win = pg.GraphicsLayoutWidget()

		# plot area (ViewBox + axes) for displaying the image
		p1 = win.addPlot(title="")

		# item for displaying image data
		img = pg.ImageItem()

		# adding image to the plot area
		p1.addItem(img)

		# Custom ROI for selecting an image region
		roi = pg.ROI([-10, 14], [5, 5])
		roi.addScaleHandle([0.5, 1], [0.5, 0.5])
		roi.addScaleHandle([0, 0.5], [0.5, 0.5])

		# adding roi to the plot area
		p1.addItem(roi)

		# setting z value to roi
		# making sure ROI is drawn above image
		roi.setZValue(10)

		# creating a Isocurve drawing on the image
		iso = pg.IsocurveItem(level=1.2, pen='r')

		# setting parent as image
		iso.setParentItem(img)

		# setting z axis value of isocurve
		iso.setZValue(5)

		# Contrast/color control
		hist = pg.HistogramLUTItem()

		# setting image to the control
		hist.setImageItem(img)

		# adding control widget to the plot window
		win.addItem(hist)

		# creating draggable line for setting isocurve level
		isoLine = pg.InfiniteLine(angle=0, movable=True, pen='r')
		hist.vb.addItem(isoLine)

		# making user interaction a little easier
		hist.vb.setMouseEnabled(y=False)
		isoLine.setValue(0.8)

		# bring iso line above contrast controls
		isoLine.setZValue(1000)

		# going to next row of grpahic window
		win.nextRow()

		# another plot area for displaying ROI data
		p2 = win.addPlot(colspan=2)

		# setting maximum height of plot area
		p2.setMaximumHeight(250)

		# generating image data
		data = np.random.normal(size=(200, 100))
		data[20:80, 20:80] += 2.

		# setting gaussian filter to the data
		data = pg.gaussianFilter(data, (3, 3))
		data += np.random.normal(size=(200, 100)) * 0.1

		# setting data to the image
		img.setImage(data)

		# setting level
		hist.setLevels(data.min(), data.max())

		# build isocurves from smoothed data
		iso.setData(pg.gaussianFilter(data, (2, 2)))

		# set position and scale of image
		img.scale(0.2, 0.2)
		img.translate(-50, 0)

		# zoom to fit image
		p1.autoRange()

		# method for updating the plot
		def updatePlot():

			# getting the selected region by the roi
			selected = roi.getArrayRegion(data, img)

			# plot the selected region
			p2.plot(selected.mean(axis=0), clear=True)

		# connecting the update plot method
		# it get called when the region is changed
		roi.sigRegionChanged.connect(updatePlot)

		# call the update plot method
		updatePlot()

		# method for updating the isocurve
		def updateIsocurve():
			# setting iso level
			iso.setLevel(isoLine.value())

		isoLine.sigDragged.connect(updateIsocurve)

		# method for image hover event
		def imageHoverEvent(event):

			# showing the position, pixel, and value under the mouse cursor
			# if cursor is not on the plot area
			if event.isExit():
				# set title as blank
				p1.setTitle("")
				return

			# getting cursor positon
			pos = event.pos()
			i, j = pos.y(), pos.x()

			# pixel values
			i = int(np.clip(i, 0, data.shape[0] - 1))
			j = int(np.clip(j, 0, data.shape[1] - 1))

			# value of point
			val = data[i, j]
			ppos = img.mapToParent(pos)
			x, y = ppos.x(), ppos.y()

			# setting plot title data
			p1.setTitle(
				"pos: (%0.1f, %0.1f) pixel: (%d, %d) value: %g" % (x, y, i, j, val))

		# Monkey-patch the image to use our custom hover function.
		img.hoverEvent = imageHoverEvent

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
