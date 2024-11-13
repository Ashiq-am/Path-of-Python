# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 15, 5)

fig1, axs1 = plt.subplots()
axs1.barbs(x ** 3, x ** 3, x * 2, x * 2, x * 3,
           fill_empty=True)

axs1.set_title('matplotlib.axes.Axes.barbs()\
Example', fontsize=14, fontweight='bold')
plt.show()
