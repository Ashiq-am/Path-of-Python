from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

with Drawing() as draw:
	draw.stroke_width = 2
	draw.stroke_color = Color('black')
	draw.fill_color = Color('white')
	draw.path_start()
	# points list to determine curve
	points = [(40, 10), # Start point
			(20, 50), # First control
			(90, 10), # Second control
			(70, 40)] # End point
	# Start middle-left
	draw.path_move(to =(10, 100))
	# Curve accross top-left to center
	draw.path_curve_to_quadratic_bezier(to =(100, 0),
					control = points,
					smooth = True,
					relative = True)
	draw.path_finish()
	with Image(width = 200,
			height = 200,
			background = Color('lightgreen')) as image:
		draw(image)
		image.save(filename ="pathbcurve.png")
