# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as statistic:
		# Invoke statistic function with statistic as median, width as 20
		# height as 10, channel as 'yellow'
		statistic.statistic('median', 20, 10, 'yellow')
		# Save the image
		statistic.save(filename ='statistic1.jpg')
