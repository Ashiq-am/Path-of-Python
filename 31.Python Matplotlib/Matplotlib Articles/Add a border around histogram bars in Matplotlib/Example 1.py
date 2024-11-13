# importing package
from matplotlib import pyplot as plt
import numpy as np

#create data
fig,ax = plt.subplots(1,1)
a = np.array([22, 87, 5, 43, 56, 73, 55,
			54, 11, 20, 51, 5, 79, 31, 27])

b = (0, 25, 50, 75, 100)

# Adjust the border color
ax.hist(a, b, edgecolor = "black")

ax.set_title("histogram - Geekforgeeks")
ax.set_xlabel('Litracy Level(%)')
ax.set_ylabel('Population(million)')

plt.show()
