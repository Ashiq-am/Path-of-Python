import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from docutils.nodes import inline
from ipywidgets import interact
matplotlib
inline

x = np.linspace(0, 5, 100)
y = np.exp(x)


# Plotting the graph for exponential function
def plot(checkbox):
    # if checkbox is ticked then scatter
    # plot will be displayed
    if checkbox:
        plt.scatter(x, y, s=5)
        plt.title('Scatter plot of exponential curve')

    # if checkbox is not ticked (by default)
    # line plot will be displayed
    else:
        plt.plot(x, y)
        plt.title('Line plot of exponential curve')

    # calling the interact function


interact(plot, checkbox=bool())
