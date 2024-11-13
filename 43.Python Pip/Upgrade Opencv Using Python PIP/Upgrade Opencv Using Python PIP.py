import cv2

# Reading the image using the function imread()
image = cv2.imread('image.jpg')

# Checking whether the image is loaded successfully or not
if image is None:
	print("Error: Failed to load image.")
else:
	# Extracting the dimentions - height and width of the image taken as input
	height, width = image.shape[:2]

	# Printing height and width of image
	print("Image Height:", height)
	print("Image Width:", width)
