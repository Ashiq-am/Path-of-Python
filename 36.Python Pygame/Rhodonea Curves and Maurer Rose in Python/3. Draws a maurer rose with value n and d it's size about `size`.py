# Draws a maurer rose with value n and d it's size about `size`
from cmath import cos
from math import sin, radians


def drawMaurerRose(n, d, size):
	points =[]
	for i in range(0, 361):
		# The equation of a maurer rose
		k = i * d
		r = size * sin(radians(n * k))

		# Converting to cartesian co-ordinates
		x = r * cos(radians(k))
		y = r * sin(radians(k))

		list.append(points, (width / 2 + x, height / 2 + y))

	# Draws a set of line segments connected by set of vertices points
	# Also don't close the path and draw it black and set the width to 5
	pygame.draw.lines(screen, (0, 0, 0), False, points, 5)

def drawPattern():
	# Try changing these values to what you want
	drawMaurerRose(6, 79, 200)
