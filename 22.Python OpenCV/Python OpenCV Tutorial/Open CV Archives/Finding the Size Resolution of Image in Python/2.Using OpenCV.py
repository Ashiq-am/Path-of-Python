# importing the module
import cv2

# loading the image
img = cv2.imread("geeksforgeeks.png")

# fetching the dimensions
wid = img.shape[1]
hgt = img.shape[0]

# displaying the dimensions
print(str(wid) + "x" + str(hgt))
