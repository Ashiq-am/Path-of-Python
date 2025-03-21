# Noise removal using Morphological
# closing operation
import cv2
from pandas import np

kernel = np.ones((3, 3), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE,kernel, iterations = 2)

# Background area using Dialation 
bg = cv2.dilate(closing, kernel, iterations = 1)

# Finding foreground area
dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0)
ret, fg = cv2.threshold(dist_transform, 0.02
						* dist_transform.max(), 255, 0)

cv2.imshow('image', fg)
