# importing opencv
import cv2

# reading the images
circle = cv2.imread('circle.png')
star = cv2.imread('star.png')

# subtract the images
subracted = cv2.subtract(star, circle)

# TO show the output
cv2.imshow('image', subracted)

# To close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
