# importing matplotlib package
import matplotlib.pyplot as plt

# importing the numpy package
import numpy as np

# Storing set of values in
# names, x, height,
# error and colors for ploting the graph
names = ['Bijon', 'Sujit', 'Sayan', 'Saikat']
x = np.arange(4)
marks = [60, 90, 55, 46]
error = [11, 15, 5, 9]
colors = ['red', 'green', 'blue', 'black']

# using tuple unpacking
# to grab fig and axes
fig, ax = plt.subplots()

# ploting the bar plot
ax.bar(x, marks, alpha=0.5,
       color=colors)

# Zip function acts as an
# iterator for tuples so that
# we are iterating through
# each set of values in a loop
for pos, y, err, colors in zip(x, marks,
                               error, colors):
    ax.errorbar(pos, y, err, lw=2,
                capsize=4, capthick=4,
                color=colors)

# Showing the plotted error bar
# plot with different color
ax.set_ylabel('Marks of the Students')

# Using x_ticks and x_labels
# to set the name of the
# students at each point
ax.set_xticks(x)
ax.set_xticklabels(names)
ax.set_xlabel('Name of the students')

# Showing the plot
plt.show()
