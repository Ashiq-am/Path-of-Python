# importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np


x = [1, 2, 3, 4, 5]
y = [11, 22, 33, 44, 55]

fig, ax = plt.subplots()
ax.semilogy(x, y)
