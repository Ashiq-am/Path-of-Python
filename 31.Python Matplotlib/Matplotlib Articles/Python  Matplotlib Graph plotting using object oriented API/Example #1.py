# importing matplotlib library
import matplotlib.pyplot as plt

# x axis values
x =[0, 5, 3, 6, 8, 4, 5, 7]

# y axis values
y =[5, 3, 6, 3, 7, 5, 6, 8]

# creating the canvas
fig = plt.figure()

# setting the size of canvas
axes = fig.add_axes([0, 0, 1, 1])

# plotting the graph
axes.plot(x, y, 'mo--')

# displaying the graph
plt.show()
