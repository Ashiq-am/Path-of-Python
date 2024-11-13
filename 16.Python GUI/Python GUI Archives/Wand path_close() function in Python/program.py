# importing wand
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
	# Curve accross top-left to center
	draw.path_curve(to =(80, 0),
					controls =[(20, -80), (60, -80)],
					relative = True)
	# Continue curve accross bottom-right
	draw.path_curve(to =(80, 0),
					controls =(60, 80),
					smooth = True,
					relative = True)
	# Join the last destination ppoint to the first point
	draw.path_close()
	draw.path_finish()
	with Image(width = 200, height = 200, background = Color('lightgreen')) as image:
		draw(image)
		image.save(filename = "pathclose.png")
