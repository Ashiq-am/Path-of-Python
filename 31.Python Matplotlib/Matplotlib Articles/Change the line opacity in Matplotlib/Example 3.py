# importing libraries
import matplotlib.pyplot as plt
import numpy as np

# create data
x = [1, 2, 3, 4, 5]

# plot
for i in range(10):
    plt.plot([1, 2.8], [i] * 2, linewidth=5, color='red', alpha=0.1 * i)
    plt.plot([3.1, 4.8], [i] * 2, linewidth=5, color='green', alpha=0.1 * i)
    plt.plot([5.1, 6.8], [i] * 2, linewidth=5, color='yellow', alpha=0.1 * i)
    plt.plot([7.1, 8.8], [i] * 2, linewidth=5, color='blue', alpha=0.1 * i)

for i in range(10):
    plt.plot([1, 2.8], [-i] * 2, linewidth=5, color='red', alpha=0.1 * i)
    plt.plot([3.1, 4.8], [-i] * 2, linewidth=5, color='green', alpha=0.1 * i)
    plt.plot([5.1, 6.8], [-i] * 2, linewidth=5, color='yellow', alpha=0.1 * i)
    plt.plot([7.1, 8.8], [-i] * 2, linewidth=5, color='blue', alpha=0.1 * i)

plt.show()
