import cv2

# read the image
img = cv2.imread('image.png')

# this is pixel of 0th row and 0th column
print(img[0][0])
