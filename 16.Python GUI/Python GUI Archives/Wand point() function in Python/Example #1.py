# Import different modules of wand
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# object for Drawing
with Drawing() as draw:
	x = 100
	y = 100
	# draw point at (100, 100) using point() function
	draw.point(x, y)

	with Image(width = 200, height = 200,
			background = Color('lightgreen')) as image:

		draw(image)
		image.save(filename ="point.png")
