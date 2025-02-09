fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.plot(x, y1)
ax2.plot(x, y2)

# Share x-axis after creation
ax2.sharex(ax1)

plt.show()