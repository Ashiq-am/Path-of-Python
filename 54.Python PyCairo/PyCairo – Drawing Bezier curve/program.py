# importing pycairo
import cairo

# creating a SVG surface
# here geek95 is file name & 700, 700 is dimension
with cairo.SVGSurface("geek95.svg", 700, 700) as surface:

	# creating a cairo context object for SVG surface
	# useing Context method
	context = cairo.Context(surface)

	# move the context to x,y position
	context.move_to(50, 200)
	# Drawing Curve
	context.curve_to(150, 75, 225, 50, 350, 150)
	# setting color of the context
	context.set_source_rgb(1, 0, 0)
	# setting width of the context
	context.set_line_width(4)
	# stroke out the color and width property
	context.stroke()

# printing message when file is saved
print("File Saved")
