import cv2

image = cv2.imread('geekslogo.png')
overlay = image.copy()

# A filled circle
cv2.circle(overlay, (250, 250), 70, (15,75,50), 20)

alpha = 0.4 # Transparency factor.

# Following line overlays transparent rectangle
# over the image
image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

cv2.imshow("some", image_new)
cv2.waitKey(0)

cv2.destroyAllWindows()
