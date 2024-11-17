import cv2
import numpy as np

# Morphology
kernel = np.ones((5, 5), dtype = np.uint8)
original_image = cv2.imread('Data/test.png')
image = cv2.morphologyEx(original_image, cv2.MORPH_CLOSE, kernel = kernel)

# resize your image according to your test image
image = cv2.resize(image, (int(750 * 0.7), int(1000 * 0.7)))
cv2.imshow("Document Scanner", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
