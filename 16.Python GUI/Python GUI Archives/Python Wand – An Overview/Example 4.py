# Import libraries from the wand
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

with Drawing() as draw:
	# Set Stroke color the circle to black
	draw.stroke_color = Color('black')

	# Set Width of the circlw to 2
	draw.stroke_width = 2

	# Set the fill color to 'White (# FFFFFF)'
	draw.fill_color = Color('white')

	# Invoke Circle function with center
	# at 200, 200 and radius 100
	draw.circle((200, 200), # Center point
				(100, 100)) # Perimeter point
	with Image(width = 400, height = 400,
			background = Color('lightgreen')) as pic:
		draw(pic)
		pic.save(filename ='circle1.jpg')
