# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as edge:
		# Invoke edge function
		edge.edge(0.1)
		# Save the image
		edge.save(filename ='edge1.jpg')
