import cv2

image = cv2.imread("/content/gfg.jpeg")
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
