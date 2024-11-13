# import Numpy and matplotlib
from matplotlib import pyplot as plt
import numpy as np


# Using predefined dataset
data_set = [45, 85, 95, 10, 58, 77, 92, 72, 52,
			22, 32, 5, 95, 2, 23, 24, 50, 40, 60,
			69, 44, 80, 21, 15, 17, 55, 21, 88]

# Creation of plot
fig = plt.figure(figsize=(10, 5))

# plotting the Histogram with certain intervals
plt.hist(data_set, bins=[0, 15, 30, 45, 60, 75, 90, 105])

# Giving title to Histogram
plt.title("Predefined Histogram")

# Displaying Histogram
plt.show()
