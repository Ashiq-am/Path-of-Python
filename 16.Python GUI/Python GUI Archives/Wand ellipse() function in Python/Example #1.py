# Import required objects from wand modules
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# generate object for wand.drawing
with Drawing() as draw:
	# set stroke color
	draw.stroke_color = Color('black')

	# set width for stroke
	draw.stroke_width = 1

	# fill white color in arc
	draw.fill_color = Color('white')
	origin = (100, 100)
	perimeter = (50, 100)

	# draw circle using circle() function
	draw.ellipse(origin, perimeter)
	with Image(width = 200,
			height = 200,
			background = Color('green')) as img:
		# draw shape on image using draw() function
		draw.draw(img)
		img.save(filename ='ellipse.png')
