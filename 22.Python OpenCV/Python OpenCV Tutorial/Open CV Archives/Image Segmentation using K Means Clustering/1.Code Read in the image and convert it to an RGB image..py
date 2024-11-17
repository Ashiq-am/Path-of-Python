import numpy as np
import matplotlib.pyplot as plt
import cv2

matplotlibinline

# Read in the image
image = cv2.imread('images/monarch.jpg')

# Change color to RGB (from BGR)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image)
