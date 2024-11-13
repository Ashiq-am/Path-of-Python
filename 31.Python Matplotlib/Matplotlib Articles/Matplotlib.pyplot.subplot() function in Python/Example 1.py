# importing hte module
import matplotlib.pyplot as plt

# Data to display on plot
x = [1, 2, 3, 4, 5]
y = [1, 2, 1, 2, 1]

# plot() will create new figure and will add axes object (plot) of above data
plt.plot(x, y, marker="x", color="green")

# subplot() will add plot to current figure deleting existing plot
plt.subplot(121)
