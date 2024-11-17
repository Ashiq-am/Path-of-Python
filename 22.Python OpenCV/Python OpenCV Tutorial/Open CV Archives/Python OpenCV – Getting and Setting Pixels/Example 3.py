# import thr cv2 package
import cv2

# read teh image
img = cv2.imread('image.png')
for i, row in enumerate(img):

# get the pixel values by iterating
	for j, pixel in enumerate(img):
		if(i == j or i+j == img.shape[0]):

				# update the pixel value to black
			img[i][j] = [0, 0, 0]

# display image
cv2.imshow("output", img)
cv2.imwrite("output.png", img)
