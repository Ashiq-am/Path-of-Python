import matplotlib.pyplot as plt


# Initilaizing values
# of x and y
x =[1, 2, 3, 4, 5]
y =[2, 4, 6, 8, 10]

# Plotting the graph
plt.plot(x, y)

# Adding an arrow to graph starting
# from the base (2, 4) and with the
# length of 2 units from both x and y
# And setting the width of arrow for
# better visualization
plt.arrow(2, 4, 2, 2, width = 0.05)

# Showing the graph
plt.show()
