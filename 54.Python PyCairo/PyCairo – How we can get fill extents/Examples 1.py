# importing pycairo
import cairo

# creating a SVG surface
# here geek1 is file name & 700, 700 is dimension
with cairo.SVGSurface("geek1.svg", 700, 700) as surface:

	# creating a cairo context object
	context = cairo.Context(surface)

	# creating a arc with using close path method
	context.arc(300, 60, 40, 0, 1*22/7)

	# makeing close path
	context.close_path()
	context.fill()

	# getting fill extends
	a = context.fill_extents()

	# stroke the context to remove the moved pen
	context.stroke()

# printing message when file is saved
print(a)
