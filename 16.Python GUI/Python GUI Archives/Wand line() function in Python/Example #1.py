# Import required objects from wand modules
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# generate object for wand.drawing
with Drawing() as draw:
	# set stroke color
	draw.stroke_color = Color('green')
	# set width for stroke
	draw.stroke_width = 1
	draw.line(( 50, 50), # Stating point
			( 150, 150)) # Ending point
	with Image(width = 200,
			height = 200,
			background = Color('white')) as img:
		# draw shape on image using draw() function
		draw.draw(img)
		img.save(filename ='line.png')
