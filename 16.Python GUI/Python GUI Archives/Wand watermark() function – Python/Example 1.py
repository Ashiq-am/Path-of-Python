# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Import the watermark image
	with Image(filename ='wave1.jpg') as water:
		# Clone the image in order to process
		with image.clone() as watermark:
			# Invoke watermark function with watermark image, transparency as 0.5
			# left as 10 and top as 20
			watermark.watermark(water, 0.5, 10, 20)
				# Save the image
			watermark.save(filename ='watermark1.jpg')
