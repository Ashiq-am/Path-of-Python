import cv2
import numpy as np

FILE_NAME = 'geeks.png'

# Read image from the disk.
img = cv2.imread(FILE_NAME)

# Shape of image in terms of pixels.
(rows, cols) = img.shape[:2]

# getRotationMatrix2D creates a matrix needed
# for transformation. We want matrix for rotation
# w.r.t center to 45 degree without scaling.
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
res = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow("GeeksforGeeks", res)

cv2.waitKey(0)
cv2.destroyAllWindows()
