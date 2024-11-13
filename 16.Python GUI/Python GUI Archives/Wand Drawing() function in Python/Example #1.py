# Import important objects from wand library
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

# Create draw object using Drawing() function
with Drawing() as draw:
	with Image(width = 200,
			height = 200,
			background = Color('green')) as img:
		draw(img)
		img.save(filename ='empty.gif')
