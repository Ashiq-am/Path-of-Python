# importing the required libraries
import cv2
import numpy as np

# reading image in grayscale
img = cv2.imread("img.jpg", cv2.IMREAD_GRAYSCALE)

# intializing web cam
cap = cv2.VideoCapture(0)
