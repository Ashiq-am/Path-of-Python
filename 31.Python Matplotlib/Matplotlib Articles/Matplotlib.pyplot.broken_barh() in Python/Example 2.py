# importing module
import matplotlib.pyplot as plt


# Adding title to the plot
plt.title('GEEKSFORGEEKS - EXAMPLE')

# adding x axis label to the plot
plt.xlabel('Number of Cars')

# label for y axis for the plot
plt.ylabel('Average Speed')

x_1 = [(10, 3), (15, 4)]
y_1 = (50, 10)

# Plotting the chart
plt.broken_barh(x_1, y_1, facecolors ='cyan')

x_2 = [(1, 4), (10, 1), (15, 4), (25, 6)]
y_2 = (70, 10)

# Plotting the chart
plt.broken_barh(x_2, y_2, facecolors ='green')

x_3 = [(5, 3), (11, 2), (18, 5)]
y_3 = (90, 10)

# Plotting the chart
plt.broken_barh(x_3, y_3, facecolors ='blue')

plt.show()
