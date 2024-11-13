# Import required objects from wand modules
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# generate object for wand.drawing
with Drawing() as draw:
	draw.fill_color = Color('blue')
	draw.alpha(10, 35, 'floodfill')
	with Image(width = 200,
			height = 200,
			background = Color('white')) as img:
		# draw shape on image using draw() function
		draw.draw(img)
		img.save(filename ='color2.png')
