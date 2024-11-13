# Import different modules of wand
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
import math

with Drawing() as draw:
	draw.fill_color = Color('GREEN')
	draw.rectangle(left = 25, top = 50, right = 175,
						bottom = 150, radius = 25)

	with Image(width = 200, height = 200, background = Color('lightgreen')) as image:
		draw(image)
		image.save(filename = "rectangle.png")
