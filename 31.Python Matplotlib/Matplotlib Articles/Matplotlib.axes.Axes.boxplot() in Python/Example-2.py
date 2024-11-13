# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10**7)

val1 = np.random.rand(50) * 80
val2 = np.ones(25) * 80
val3 = np.random.rand(25) * 80 + 100
val4 = np.random.rand(25) * -80
data = np.concatenate((val1, val2, val3, val4))
data1 = np.concatenate((val2, val4, val1, val3))
data = [data, data1]

fig1, ax1 = plt.subplots()
ax1.boxplot(data, notch = True, vert = False, whis = 0.75)

ax1.set_title('matplotlib.axes.Axes.boxplot() Example')
plt.show()
