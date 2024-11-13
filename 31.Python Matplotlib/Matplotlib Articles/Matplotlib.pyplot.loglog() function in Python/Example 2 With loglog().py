# importing requried modules
import matplotlib.pyplot as plt
import numpy as np


# inputs to plot using loglog plot
x_input = np.linspace(0, 10, 50000)

y_input = x_input**8

# plotting the value of x_input and y_input using loglog plot
plt.loglog(x_input, y_input)
