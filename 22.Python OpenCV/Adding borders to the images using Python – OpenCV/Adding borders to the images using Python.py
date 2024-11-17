# importing required packages

import cv2

# reading the image
virat_img = cv2.imread('geek.jpg')

# making border around image using copyMakeBorder
borderoutput = cv2.copyMakeBorder(
	virat_img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[255, 255, 0])

# showing the image with border
cv2.imwrite('output list views.png', borderoutput)
