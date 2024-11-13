# importing pycairo
import cairo

# creating a SVG surface
# here geek95 is file name & 700, 700 is dimension
with cairo.SVGSurface("geek95.svg", 700, 700) as surface:

	# creating a cairo context object for SVG surface
	# useing Context method
	context = cairo.Context(surface)
	context.set_source_rgba(0, 0, 0, 1)
	context.set_line_width(12)

	# Translate the context
	context.translate(60, 60)

	# Creating a Radial gradient object.
	r1 = cairo.RadialGradient(30, 30, 10, 30, 30, 90)
	r1.add_color_stop_rgba(0, 1, 1, 1, 1)
	r1.add_color_stop_rgba(1, 0.6, 0.6, 0.6, 1)
	context.set_source(r1)

	# Creating Circle
	context.arc(0, 0, 40, 0, 3.14 * 2)

	# Fill the color inside the Circle
	context.fill()

# printing message when file is saved
print("File Saved")
