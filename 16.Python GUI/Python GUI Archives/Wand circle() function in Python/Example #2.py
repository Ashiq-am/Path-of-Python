# Import required objects from wand modules
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# generate object for wand.drawing
with Drawing() as draw:
	origin = (100, 100)
	perimeter = (50, 50)

	# set stroke color
	draw.stroke_color = Color('black')

	# set width for stroke
	draw.stroke_width = 1

	# fill white color in arc
	draw.fill_color = Color('white')

	# draw bezier curve using bezier function
	draw.circle(origin, perimeter)
	with Image(filename ="gog.png") as img:

		# draw shape on image using draw() function
		draw.draw(img)
		img.save(filename ='circle2.png')
