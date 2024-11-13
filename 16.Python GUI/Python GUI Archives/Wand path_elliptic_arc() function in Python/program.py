from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

with Drawing() as draw:
	draw.stroke_width = 2
	draw.stroke_color = Color('black')
	draw.fill_color = Color('white')
	draw.path_start()
	# Start middle-left
	draw.path_move(to =(10, 100))
	# draw elliptical curve
	draw.path_elliptic_arc(to =(10, 180),
						radius = (20, 40),
						rotation = 270,
						large_arc = True,
						clockwise = True,
						relative = True )
	with Image(width = 200, height = 200, background = Color('lightgreen')) as image:
		draw(image)
		image.save(filename ="pathecurve.png")
