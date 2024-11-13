from matplotlib.ticker import MultipleLocator
data = [1, 2, 3, 4, 5]
fig, ax = plt.subplots()
ax.plot(data)

# Set minor tick locations on the y-axis
ax.yaxis.set_minor_locator(MultipleLocator(0.1))
# Enable grid for minor ticks
ax.grid(which='both', linestyle='--', linewidth=0.5)
plt.show()
