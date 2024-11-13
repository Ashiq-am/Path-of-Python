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
	draw.arc(( 50, 50), # Stating point
			( 150, 150), # Ending point
			(135, -45)) # From bottom left around to top right
	with Image(width = 100,
			height = 100,
			background = Color('green')) as img:
		# draw shape on image using draw() function
		draw.draw(img)
		img.save(filename ='arc.png')
