# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10 ** 7)

x1 = np.random.rand(103, 53)

plt.title('matplotlib.pyplot.ginput() function\
Example', fontweight="bold")

print("After 2 clicks :")
plt.imshow(x1)
x = plt.ginput(2)
print(x)

plt.show()
