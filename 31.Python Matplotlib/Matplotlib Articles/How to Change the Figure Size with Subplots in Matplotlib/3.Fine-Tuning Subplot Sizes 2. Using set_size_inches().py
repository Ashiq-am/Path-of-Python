import matplotlib.pyplot as plt

# Create a figure and plot some data
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 9, 16])

# Dynamically adjust the figure size
fig.set_size_inches(4,3)
plt.show()
