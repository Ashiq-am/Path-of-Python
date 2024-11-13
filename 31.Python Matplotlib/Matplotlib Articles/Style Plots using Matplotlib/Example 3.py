# importing all the necessary packages
import numpy as np
import matplotlib.pyplot as plt

# importing the style package
from matplotlib import style

# creating an array of data for plot
data = np.random.randn(50)

# using the style for the plot
plt.style.use('ggplot')

# creating plot
plt.plot(data, linestyle=":", linewidth=2)

# show plot
plt.show()
