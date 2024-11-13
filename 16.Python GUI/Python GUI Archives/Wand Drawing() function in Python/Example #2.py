# Import important objects from wand library
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# Create draw object using Drawing() function
with Drawing() as draw:
	draw.stroke_color = Color('black')
	draw.stroke_width = 2
	draw.line((5, 5), (45, 50))
	with Image(width = 200,
			height = 200,
			background = Color('green')) as img:
		draw.draw(img)
		img.save(filename ='line.gif')
