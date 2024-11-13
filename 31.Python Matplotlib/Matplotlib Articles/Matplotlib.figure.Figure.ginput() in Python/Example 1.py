# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(10)

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

ax.plot(t, np.sin(t))

fig.suptitle('matplotlib.figure.Figure.ginput() \
function Example', fontweight="bold")

print("After 3 clicks :")
x = fig.ginput(3)
print(x)

plt.show()
