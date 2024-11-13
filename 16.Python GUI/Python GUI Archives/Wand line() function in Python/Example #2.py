# Import required objects from wand modules
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# generate object for wand.drawing
with Drawing() as draw:
	# set stroke color
	draw.stroke_color = Color('white')

	# set width for stroke
	draw.stroke_width = 1
	with Image(filename = "gog.png") as img:
		draw.line((( img.height)/2, 0), # Stating point
				( 0, (img.width)/2)) # Ending point

		# draw shape on image using draw() function
		draw.draw(img)
		img.save(filename ='line2.png')
