# importing matplotlib
import matplotlib.pyplot as plt

# importing the numpy package
import numpy as np

# Storing set of values in
# names, x, height, error,
# error1 and colors for ploting the graph
names = ['USA', 'India', 'England', 'China']
x = np.arange(4)
economy = [21.43, 2.87, 2.83, 14.34]
error = [1.4, 1.5, 0.5, 1.9]
error1 = [0.5, 0.2, 0.6, 1]
colors = ['red', 'grey', 'blue', 'magenta']

# using tuple unpacking
# to grab fig and axes
fig, ax = plt.subplots()

# ploting the bar plot
ax.bar(x, economy, alpha=0.5,
       color=colors)

# Zip function acts as an
# iterator for tuples so that
# we are iterating through
# each set of values in a loop
for pos, y, err, err1, colors in zip(x, economy,
                                     error, error1,
                                     colors):
    ax.errorbar(pos, y, err, err1, fmt='o',
                lw=2, capsize=4, capthick=4,
                color=colors)

# Showing the plotted error bar
# plot with different color
ax.set_ylabel('Economy(in trillions)')

# Using x_ticks and x_labels
# to set the name of the
# countries at each point
ax.set_xticks(x)
ax.set_xticklabels(names)
ax.set_xlabel('Name of the countries')

# Showing the plot
plt.show()
