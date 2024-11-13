from itertools import chain
# Import Color from wand.color module
from wand.color import Color
# Import Image from wand.image module
from wand.image import Image

with Image(filename ='gog.png') as img:
	img.background_color = Color('skyblue')
	img.virtual_pixel = 'background'
	sp = (
		(0, 0),
		(140, 0),
		(0, 92),
		(140, 92)
	)
	dp = (
		(14, 4.6),
		(126.9, 9.2),
		(0, 92),
		(140, 92)
	)
	order = chain.from_iterable(zip(sp, dp))
	arguments = list(chain.from_iterable(order))
	img.distort('perspective', arguments)
	img.save(filename ='gfg_p2.png')
