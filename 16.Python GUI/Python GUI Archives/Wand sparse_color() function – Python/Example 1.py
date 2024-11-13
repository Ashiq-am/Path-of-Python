# Import library from Image
from wand.image import Image
from wand.color import Color
colors = {
Color('RED'): (100, 150),
Color('YELLOW'): (250, 150),
Color('ORANGE'): (300, 123)
}

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as sparse_color:
		# Invoke sparse_color function with 'bilinear' method
		sparse_color.sparse_color('bilinear', colors)
		# Save the image
		sparse_color.save(filename ='sparse_color1.jpg')
