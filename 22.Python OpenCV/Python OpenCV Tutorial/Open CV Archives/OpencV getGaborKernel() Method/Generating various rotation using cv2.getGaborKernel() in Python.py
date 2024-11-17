# Import required libraies
import cv2
import numpy as np
import matplotlib.pyplot as plt

# kernel size
ksize = 31
# sigma for Gaussian envelope
sigma = 5
# range of orientation values
theta_range = np.arange(0, np.pi, np.pi / 4)
# frequency of sinusoidal wave
frequency = 0.3
# phase of sinusoidal wave
phase = 0

# for loop for generating different rotation
for theta in theta_range:
	kernel = cv2.getGaborKernel((ksize, ksize),
								sigma, theta,
								frequency, phase)
	plt.imshow(kernel,
			cmap='gray')
	plt.title("Kernel with orientation = " + str(theta))
	plt.show()
