from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

with Drawing() as draw:
	draw.stroke_width = 2
	draw.stroke_color = Color('black')
	draw.fill_color = Color('white')
	draw.path_start()
	# set starting point for first sub-path
	draw.path_move(to =(10, 10))
	# Drawing vertical line from start
	draw.path_vertical_line(100,
							relative = True)
	# set starting point for second sub-path
	draw.path_move(to =(190, 10))
	# Drawing vertical line from start
	draw.path_vertical_line(100,
							relative = True)
	draw.path_finish()
	with Image(width = 200, height = 200, background = Color('lightgreen')) as image:
		draw(image)
		image.save(filename ="pathmove.png")
