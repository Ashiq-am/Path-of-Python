import cv2

image = cv2.imread('test.jpg')
overlay = image.copy()

# Rectangle parameters
x, y, w, h = 10, 10, 300, 300
# A filled rectangle
cv2.rectangle(overlay, (x, y), (x+w, y+h), (0, 200, 0), -1)

alpha = 0.4 # Transparency factor.

# Following line overlays transparent rectangle
# over the image
image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

cv2.imshow("some", image_new)
cv2.waitKey(0)

cv2.destroyAllWindows()
