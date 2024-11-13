# importing the required libraries
import numpy as np
import matplotlib.pyplot as plt

# function that will
# ouput the values
def function(t):
	return np.exp(-t)*np.sin(2*np.pi.t)/2 + np.tan(t)

# define the x-axis values
t1 = np.arange(-0.01, 1.0, 0.08)
t2 = np.arange(0.0, 5.0, 0.02)


# subplot 1
plt.figure(figsize = (10,10))
plt.subplot(211)

# plot the graph
plt.semilogx(t1, f(t1),
			'bo', t2, f(t2),
			'k', color = "blue",
			basex = 3)
# set the title
plt.title("BASE: 3")

# subplot 2
plt.subplot(212)

# plot the graph
plt.semilogx(t2, np.cos(2*np.pi*t2),
			'r--', color = "brown",
			linewidth = 2, basex = 4)

# set the title
plt.title("BASE: 4")

# show the plot
plt.show()
