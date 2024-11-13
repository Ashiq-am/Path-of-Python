# importing packages
import matplotlib.pyplot as plt
import numpy as np

# create data
x_values = np.linspace(0, 10, 20)
y_values = np.sin(x_values)
markers = ['>', '+', '.', ',', 'o', 'v', 'x', 'X', 'D', '|']

# apply markers
for i in range(20):
	plt.plot(x_values, y_values + i*0.2, markers[i % 10])
plt.show()
