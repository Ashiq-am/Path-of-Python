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

	# points list to determine curve
	points = [(40, 10), # Start point
			(20, 50), # First control
			(90, 10), # Second control
			(70, 40)] # End point

	# fill white color in arc
	draw.fill_color = Color('white')

	# draw bezier curve using bezier function
	draw.bezier(points)
	with Image(width = 100,
			height = 100,
			background = Color('green')) as img:

		# draw shape on image using draw() function
		draw.draw(img)
		img.save(filename ='bezier.png')
