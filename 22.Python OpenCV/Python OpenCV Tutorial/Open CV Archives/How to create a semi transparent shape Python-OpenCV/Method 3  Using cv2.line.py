import cv2

image = cv2.imread('geekslogo.png')
overlay = image.copy()

# A filled line
cv2.line(overlay, (0,0), (311,211), (0,355,0),40)

# Transparency factor.
alpha = 0.4

# Following line overlays transparent rectangle
# over the image
image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

cv2.imshow("some", image_new)
cv2.waitKey(0)

cv2.destroyAllWindows()
