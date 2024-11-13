# Draws a rose with n petals and of radius size about `size`
def drawRhodoneaCurve(n, size):
	points =[]
	for i in range(0, 361):
		# The equation of a rhodonea curve
		r = size * sin(radians(n * i))

		# Converting to cartesian co-ordinates
		x = r * cos(radians(i))
		y = r * sin(radians(i))

		list.append(points, (width / 2 + x, height / 2 + y))

	# Draws a set of line segments connected by set of vertices points
	# Also don't close the path and draw it black and set the width to 5
	pygame.draw.lines(screen, (0, 0, 0), False, points, 5)

def drawPattern():
	# Try changing these values to what you want
	drawRhodoneaCurve(12, 200)
