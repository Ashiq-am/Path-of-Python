import matplotlib.pyplot as plt

# Turn off interactive mode
plt.ioff()
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Interactive Mode Disabled")

# The plot won't display automatically Save the plot instead
plt.savefig("plot.png")