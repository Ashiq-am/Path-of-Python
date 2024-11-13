# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10 ** 7)

x1 = np.random.rand(103, 53)
fig = plt.figure(dpi=100)
axes = fig.add_subplot(111)

fig.suptitle('matplotlib.figure.Figure.ginput() \
function Example', fontweight="bold")

print("After 2 clicks :")
axes.imshow(x1)
x = fig.ginput(2)
print(x)

plt.show()
