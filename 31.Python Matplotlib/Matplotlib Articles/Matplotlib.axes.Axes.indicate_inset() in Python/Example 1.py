# Implementation of matplotlib function
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(range(10))
axin1 = ax.indicate_inset([0.8, 0.1, 0.5, 0.5])
axin2 = ax.indicate_inset(
    [5, 7, 2.3, 2.3], transform=ax.transData)
ax.set_title('matplotlib.axes.Axes.indicate_inset() Example',
             fontsize=14, fontweight='bold')
plt.show()
