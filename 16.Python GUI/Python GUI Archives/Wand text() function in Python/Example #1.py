# Import different modules of wand
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
import math

with Drawing() as draw:
	with Image(width = 200, height = 200, background = Color('lightgreen')) as image:

		draw.font = 'wandtests/assets/League_Gothic.otf'
		draw.font_size = 10
		draw.text(image.width / 2, image.height / 2, 'GeeksForGeeks')
		draw(image)
		image.save(filename = "text.png")
