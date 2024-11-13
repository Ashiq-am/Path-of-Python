# Import library from Image
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as wavelet_denoise:
		# Invoke wavelet_denoise function with threshold as 10
		# softness as 15
		wavelet_denoise.wavelet_denoise(10, 15)
		# Save the image
		wavelet_denoise.save(filename ='wavelet_denoise1.jpg')
