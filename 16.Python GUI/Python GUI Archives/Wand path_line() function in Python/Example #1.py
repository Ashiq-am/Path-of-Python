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

	# Continue path to right
	draw.path_line(to =(100, 0),
					relative = True)

	# Continue path to bottom left
	draw.path_line(to =(10, 80),
					relative = True)
	draw.path_finish()
	with Image(width = 200, height = 200, background = Color('lightgreen')) as image:
		draw(image)
		image.save(filename ="pathline.png")
