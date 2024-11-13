# Import different modules of wand
from kivy.multistroke import xrange
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
import math

with Drawing() as draw:
	for x in xrange(0, 200):
		y = math.tan(x) * 4
		# draw points at different locations using point() function
		draw.point(x, y + 50)
	with Image(width = 200, height = 200, background = Color('lightgreen')) as image:
		draw(image)
		image.save(filename = "points.png")
