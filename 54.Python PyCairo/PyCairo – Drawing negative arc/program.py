# importing pycairo
import cairo

# creating a SVG surface
# here geek1 is file name & 700, 700 is dimension
with cairo.SVGSurface("geek1.svg", 700, 700) as surface:

	# creating a cairo context object
	context = cairo.Context(surface)

	# creating a normal arc
	context.arc(100, 60, 40, 0, 1*22/7)

	# stroke the context to remove the moved pen
	context.stroke()

	# creating a negative arc
	context.arc_negative(500, 60, 40, 0, 1*22/7)

	# stroke the context to remove the moved pen
	context.stroke()

	# printing message when file is saved
print("File Saved")
