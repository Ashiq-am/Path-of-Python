# import matplotlib lirary
import matplotlib.pyplot as plt
import numpy as np

# float lists for cross
# correlation
x, y = np.random.randn(2, 100)

# Plot graph
fig = plt.figure()
ax1 = fig.add_subplot(211)

# cross correlation using xcorr()
# function
ax1.xcorr(x, y, usevlines=True,
		maxlags=50, normed=True,
		lw=2)

# adding grid to the graph
ax1.grid(True)
ax1.axhline(0, color='blue', lw=2)

# show final plotted graph
plt.show()
