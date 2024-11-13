from collections import namedtuple
# Import Color from wand.color module
from wand.color import Color
# Import Image from wand.image module
from wand.image import Image

Point = namedtuple('Point', ['x', 'y'])

with Image(filename ='gog.png') as img:
	img.background_color = Color('skyblue')
	img.virtual_pixel = 'background'
	rotate = Point(0.1, 0)
	scale = Point(0.7, 0.6)
	translate = Point(5, 5)
	args = (
		scale.x, rotate.x, rotate.y,
		scale.y, translate.x, translate.y
	)
	img.distort('affine_projection', args)
	img.save(filename ="afflinegfg.png")
