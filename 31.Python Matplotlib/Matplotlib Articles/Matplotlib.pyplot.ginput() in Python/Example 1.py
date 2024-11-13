# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(10)

plt.plot(t, np.sin(t))

plt.title('matplotlib.pyplot.ginput()\
function Example', fontweight="bold")

print("After 3 clicks :")
x = plt.ginput(3)
print(x)

plt.show()
