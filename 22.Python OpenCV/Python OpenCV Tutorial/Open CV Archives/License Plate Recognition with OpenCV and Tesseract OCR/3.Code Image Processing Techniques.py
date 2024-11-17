# Read the license plate file and display it
import os

import cv2
from pint.testsuite.test_matplotlib import plt

test_license_plate = cv2.imread(os.getcwd() + "/license-plates / GWT2180.jpg")
plt.imshow(test_license_plate)
plt.axis('off')
plt.title('GWT2180 license plate')
