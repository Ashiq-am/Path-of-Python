from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

with Drawing() as draw:
	draw.stroke_width = 2
	draw.stroke_color = Color('black')
	draw.fill_color = Color('white')

	# points list for polygon
	points = [(25, 25), (175, 100), (25, 175)]

	# draw polygon using polygon() function
	draw.polyline(points)
	with Image(width = 200, height = 200, background = Color('lightgreen')) as image:
		draw(image)
		image.save(filename = "polygon.png")
