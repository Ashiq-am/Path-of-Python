# import matplotlib package
import matplotlib.pyplot as plt

# Store set of values in x
# and height for plotting
# the graph
x = range(4)
height = [3, 6, 5, 4]

# using tuple unpacking
# to grab fig and axes
fig, ax = plt.subplots()

# Creating the bar plot
# with opacity=0.1
ax.bar(x, height, alpha=0.1)

# Zip function acts as an
# iterator for tuples so that
# we are iterating through
# each set of values in a loop

for pos, y, err in zip(x, height, error):
    ax.errorbar(pos, y, err, lw=2,
                capsize=4, capthick=4,
                color="green")

# Showing the plotted error bar
# plot with same color which is
# green
plt.show()
