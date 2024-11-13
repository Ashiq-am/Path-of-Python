# importing pycairo
import cairo
# importing Math to Sin & exp Function
import math

# Variable X
x = 0
# Creating list for creating points
points = []
# Creating Loop for points
while x < 5:
	# Creating point corresponding x
	y = math.sin(10*x)*math.exp(-x/2)
	# Adding points to the list
	points.append((x*100 + 50, y*100 + 200))
	# Incrementing by 0.01 Variable x
	x += 0.01

# creating a SVG surface
# here geek95 is file name & 700, 700 is dimension
with cairo.SVGSurface("geek95.svg", 700, 700) as surface:

	# creating a cairo context object for SVG surface
	# useing Context method
	context = cairo.Context(surface)

	context.move_to(*points[0])
	# Traversing Points
	for p in points[1:]:
		# Ploting point
		context.line_to(*p)

	# setting width of the context
	context.set_line_width(2)
	# setting color of the context
	context.set_source_rgb(0.2, 1, 0.2)
	# stroke out the color and width property
	context.stroke()

# printing message when file is saved
print("File Saved")
