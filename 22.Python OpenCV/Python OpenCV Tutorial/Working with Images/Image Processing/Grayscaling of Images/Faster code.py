# Faster method
import cv2

# The second argument zero specifies that
# image is to be read in grayscale mode.
img = cv2.imread('C:\\Documents\\full_path\\tomatoes.jpg', 0)

cv2.imshow('Grayscale', img)
cv2.waitKey()

cv2.destroyAllWindows()
