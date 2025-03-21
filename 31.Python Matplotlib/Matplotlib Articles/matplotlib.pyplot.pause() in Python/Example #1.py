# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19)
data = np.random.random((5, 10, 10))


for i in range(len(data)):
	plt.cla()
	plt.title('matplotlib.pyplot.pause() function Example\n\n Window {}'.format(i), fontweight ="bold")
	plt.imshow(data[i])
	plt.pause(0.1)
