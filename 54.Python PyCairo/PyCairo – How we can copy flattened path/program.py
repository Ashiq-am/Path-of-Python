# importing pycairo
import cairo

# creating a SVG surface
# here geek1 is file name & 700, 700 is dimension
with cairo.SVGSurface("geek1.svg", 700, 700) as surface:

	# creating a cairo context object
	context = cairo.Context(surface)

	# creating a arc without using closing path method
	context.arc(100, 60, 40, 0, 1*22/7)

	# stroke the context to remove the moved pen
	context.stroke()

	# creating a arc with using close path method
	context.arc(300, 60, 40, 0, 1*22/7)

	# makeing close path
	context.close_path()

	# Gets a flattened copy of the current path
	c = context.copy_path_flat()

	# stroke the context to remove the moved pen
	context.stroke()

# printing message when file is saved
print(c)
