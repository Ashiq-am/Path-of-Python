# Python script to convert the given image
# into a dotted text using opencv

# import the required modules
import cv2

# Read the image
img = cv2.imread('mic.jpg', 0)

# Apply median blur
img = cv2.medianBlur(img, 5)

# Apply MEAN thresholding to get refined edges
image = cv2.adaptiveThreshold(
	img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Convert the image into a compatible size
# We will use 60 pixels wide image so that text
# fits in the console

# Preserve the ratio
ratio = len(image)/len(image[0])
# Assign new width and calculate new height
new_width = 60
new_height = int(ratio*new_width)
# Resize the image
image = cv2.resize(image, (new_height, new_width))

# Iterate over the array and print the dark pixels
# or we can use any other symbol too.
for i in range(len(image)):
	for j in range(len(image[0])):
		print("o" if image[i, j] < 100 else ".", end="")
	print()
