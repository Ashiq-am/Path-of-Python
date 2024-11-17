import cv2
from skimage.exposure import is_low_contrast

img = cv2.imread("low_contrast_img(1).jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

if (is_low_contrast(gray, 0.35)):
    cv2.putText(img, "low contrast image", (5, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                (0, 0, 0), 2)
else:
    cv2.putText(img, "high contrast image", (5, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                (0, 0, 0), 2)

cv2.imshow("output", img)
cv2.imwrite("output.jpg", img)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()
