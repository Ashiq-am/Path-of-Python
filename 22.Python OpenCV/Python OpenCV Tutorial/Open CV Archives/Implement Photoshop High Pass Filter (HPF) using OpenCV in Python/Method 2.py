import cv2
import numpy as np
import matplotlib.pyplot as plt

# read image
img = cv2.imread("naruto.jpeg")

# resize image
img = cv2.resize(img, (500, 450), interpolation=cv2.INTER_CUBIC)

# convert image to gray scale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply laplacian blur
laplacian = cv2.Laplacian(gray, cv2.CV_64F)

# sobel x filter where dx=1 and dy=0
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=7)

# sobel y filter where dx=0 and dy=1
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=7)

# combine sobel x and y
sobel = cv2.bitwise_and(sobelx, sobely)

# plot images
plt.subplot(2, 2, 1)
plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian')

plt.subplot(2, 2, 2)
plt.imshow(sobelx, cmap='gray')
plt.title('SobelX')

plt.subplot(2, 2, 3)
plt.imshow(sobely, cmap='gray')
plt.title('SobelY')

plt.subplot(2, 2, 4)
plt.imshow(sobel, cmap='gray')
plt.title('Sobel')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
