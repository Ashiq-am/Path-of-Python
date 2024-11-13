from matplotlib.ticker import MultipleLocator, FormatStrFormatter
data = [1, 2, 3, 4, 5]
fig, ax = plt.subplots(figsize=(5, 8))
ax.plot(data)

# Set minor tick locations on the y-axis
ax.yaxis.set_minor_locator(MultipleLocator(0.1))

# Format minor tick labels on the y-axis
ax.yaxis.set_minor_formatter(FormatStrFormatter('%.2f'))
# Enable grid for minor ticks
ax.grid(which='both', linestyle='--', linewidth=0.5)
plt.show()
