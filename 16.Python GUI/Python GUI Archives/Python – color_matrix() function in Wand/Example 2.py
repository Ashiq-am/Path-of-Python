# Import Image from wand.image module
from wand.image import Image

# Read image using Image function
with Image(filename ="koala.jpeg") as img:
	matrix = [[0, 1, 0],
			[1, 0, 0],
			[0, 0, 1]]
	# Recalculate color using color_matrix() method
	img.color_matrix(matrix)
	img.save(filename ="cm_koala2.jpeg")
