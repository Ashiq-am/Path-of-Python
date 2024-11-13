# import matplotlib package
import matplotlib.pyplot as plt

# Store set of values in x
# and height for plotting
# the graph
x = range(4)
height = [ 3, 6, 5, 4]

# using tuple unpacking
# to grab fig and axes
fig, ax = plt.subplots()

# Creating the bar plot
# with opacity=0.1
ax.bar(x, height, alpha = 0.1)
