# import cv2 module
import cv2

# resd the image
img = cv2.imread('image.png')

# shape prints the tuple (height,weight,channels)
print(img.shape)

# img will be a numpy array of the above shape
print(img)
