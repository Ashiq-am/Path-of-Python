# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10**7)

val1 = np.random.rand(50) * 80
val2 = np.ones(80) * 50
val3 = np.random.rand(50) * 80 + 100
val4 = np.random.rand(50) * -80
data = np.concatenate((val1, val2, val3, val4))

fig1, ax1 = plt.subplots()
ax1.boxplot(data)

ax1.set_title('matplotlib.axes.Axes.boxplot() Example')
plt.show()
