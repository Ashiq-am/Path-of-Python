import cv2

image = cv2.imread('test.jpg')
overlay = image.copy()

# Rectangle parameters
x, y, w, h = 10, 10, 300, 300

# A filled rectangle
cv2.rectangle(overlay, (x, y), (x+w, y+h), (0, 200, 0), -1)

cv2.imshow("some", overlay)
cv2.waitKey(0)

cv2.destroyAllWindows()
