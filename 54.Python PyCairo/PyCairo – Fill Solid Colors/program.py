# importing pycairo
import cairo

# creating a SVG surface
# here geek95 is file name & 700, 700 is dimension
with cairo.SVGSurface("geek95.svg", 700, 700) as surface:

	# creating a cairo context object for SVG surface
	# useing Context method
	context = cairo.Context(surface)

	# setting color of the context
	context.set_source_rgb(0.2, 0.23, 0.9)
	# creating a rectangle
	context.rectangle(10, 15, 90, 60)

	# Fill the color inside the rectangle
	context.fill()

	# setting color of the context
	context.set_source_rgb(0.9, 0.1, 0.1)
	# creating a rectangle
	context.rectangle(130, 15, 90, 60)

	# Fill the color inside the rectangle
	context.fill()

	# setting color of the context
	context.set_source_rgb(0.4, 0.9, 0.4)
	# creating a rectangle
	context.rectangle(250, 15, 90, 60)

	# Fill the color inside the rectangle
	context.fill()

	# printing message when file is saved
	print("File Saved")
