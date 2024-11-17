import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Read the image
input_image = cv.imread('rose.jpg')

# Convert the image to grayscale
gray_image = cv.cvtColor(input_image, cv.COLOR_BGR2GRAY)

# Plotting
fig, ax = plt.subplots(1, 2, figsize=(16, 8))
fig.tight_layout()

# Display original image
ax[0].imshow(cv.cvtColor(input_image, cv.COLOR_BGR2RGB))
ax[0].set_title("Original Image")

# Display grayscale image
ax[1].imshow(gray_image, cmap='gray')
ax[1].set_title("Grayscale Image")

plt.show()
