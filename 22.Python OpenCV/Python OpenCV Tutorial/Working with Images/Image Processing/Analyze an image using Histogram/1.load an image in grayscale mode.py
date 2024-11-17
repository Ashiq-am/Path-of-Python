# load an image in grayscale mode
import cv2

img = cv2.imread('ex.jpg',0)

# calculate frequency of pixels in range 0-255
histg = cv2.calcHist([img],[0],None,[256],[0,256])
