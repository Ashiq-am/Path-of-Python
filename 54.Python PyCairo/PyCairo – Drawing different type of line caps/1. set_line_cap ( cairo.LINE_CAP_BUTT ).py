# importing pycairo
import cairo

# creating a SVG surface
# here geek94 is file name & 700, 700 is dimension
with cairo.SVGSurface("geek94.svg", 700, 700) as surface:

	# creating a cairo context object for SVG surface
	# useing Context method
	context = cairo.Context(surface)
	context.set_source_rgba(0, 0, 0, 1)
	context.set_line_width(12)

	context.set_line_cap(cairo.LINE_CAP_BUTT)
	context.move_to(30, 50)
	context.line_to(150, 50)

	# stroke out the color and width property
	context.stroke()

	# printing message when file is saved
	print("File Saved")
