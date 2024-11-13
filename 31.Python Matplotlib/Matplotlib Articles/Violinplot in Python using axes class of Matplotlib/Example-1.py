# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

# create test data
np.random.seed(10**7)
data = np.random.normal(0, 5, 100)

fig, ax1 = plt.subplots()
val = ax1.violinplot(data)

ax1.set_title('matplotlib.axes.Axes.violinplot() Example')
plt.show()
