# importing matplotlib
import matplotlib.pyplot as plt

# Storing set of values in
# x, height, error and colors for ploting the graph
x = range(4)
height = [3, 6, 5, 4]
error = [1, 5, 3, 2]
colors = ['red', 'green', 'blue', 'black']

# using tuple unpacking
# to grab fig and axes
fig, ax = plt.subplots()

# ploting the bar plot
ax.bar(x, height, alpha=0.1)

# Zip function acts as an
# iterator for tuples so that
# we are iterating through
# each set of values in a loop
for pos, y, err, colors in zip(x, height,
                               error, colors):
    ax.errorbar(pos, y, err, lw=2,
                capsize=4, capthick=4,
                color=colors)

# Showing the plotted error bar
# plot with different color
plt.show()
