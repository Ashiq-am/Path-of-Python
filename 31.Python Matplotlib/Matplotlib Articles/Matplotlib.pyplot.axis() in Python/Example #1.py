import matplotlib.pyplot as plt


x =[1, 2, 3, 4, 5]
y =[2, 4, 6, 8, 10]

# Plotting the graph
plt.plot(x, y)

# Setting the x-axis to 1-10
# and y-axis to 1-15
plt.axis([0, 10, 1, 15])

# Showing the graph with updated axis
plt.show()
