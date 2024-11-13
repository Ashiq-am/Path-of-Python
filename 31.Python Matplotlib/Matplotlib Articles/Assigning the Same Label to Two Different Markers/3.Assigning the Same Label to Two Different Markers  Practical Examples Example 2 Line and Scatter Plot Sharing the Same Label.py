import matplotlib.pyplot as plt
import numpy as np
from matplotlib.legend_handler import HandlerTuple

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plotting the data with line and scatter plot
line1, = plt.plot(x, y1, 'o', label='Sine and Cosine')
scatter2 = plt.scatter(x, y2, marker='^')

# Creating custom legend handles
handles = [(line1, scatter2)]
labels = ['Sine and Cosine']

# Adding the custom legend
plt.legend(handles, labels, handler_map={tuple: HandlerTuple(ndivide=None)})
plt.show()
