# importing modules
import numpy as np
import matplotlib.pyplot as plt

# creating dataset
data = [44, 27, 5, 2, 43, 56, 77, 53, 89, 54, 11, 23, 51, 5, 79, 25, 39]

# creating class interval
classInterval = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# calculating frequency and intervals
values, base = np.histogram(data, bins=classInterval)

# calculating cumulative frequency
cumsum = np.cumsum(values)

# reversing cumulative frequency
res = np.flipud(cumsum)

# plotting ogive
plt.plot(base[1:], res, color='brown', marker='o', linestyle='-')

# formatting the graph
plt.title('Ogive Graph')
plt.xlabel('Marks in End-Term')
plt.ylabel('Cumulative Frequency')
