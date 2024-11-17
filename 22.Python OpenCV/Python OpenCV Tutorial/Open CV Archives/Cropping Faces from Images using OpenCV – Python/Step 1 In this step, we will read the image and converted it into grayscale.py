import cv2

# Read the input image
img = cv2.imread('mpw.jpeg')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
