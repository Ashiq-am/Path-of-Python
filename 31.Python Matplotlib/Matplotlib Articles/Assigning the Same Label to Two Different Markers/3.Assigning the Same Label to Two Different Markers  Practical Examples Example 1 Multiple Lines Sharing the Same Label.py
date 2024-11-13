import matplotlib.pyplot as plt
import numpy as np
from matplotlib.legend_handler import HandlerTuple

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) + np.cos(x)

# Plotting the data with different markers
line1, = plt.plot(x, y1, 'o', label='Combined Functions')
line2, = plt.plot(x, y2, '^')
line3, = plt.plot(x, y3, 's')

# Creating custom legend handles
handles = [(line1, line2, line3)]
labels = ['Combined Functions']

# Adding the custom legend
plt.legend(handles, labels, handler_map={tuple: HandlerTuple(ndivide=None)})
plt.show()
