# importing matplotlib library
import matplotlib.pyplot as plt

# x-axis values
x =[0, 1, 2, 3, 4, 5, 6]

# y-axis values
y =[0, 1, 3, 6, 9, 12, 17]

# creating the canvas
fig = plt.figure()

# setting size of first canvas
axes1 = fig.add_axes([0, 0, 0.7, 1])

# plotting graph of first canvas
axes1.plot(x, y, 'mo--')

# setting size of second canvas
axes2 = fig.add_axes([0.1, 0.5, 0.3, 0.3])

# plotting graph of second canvas
axes2.plot(x, y, 'go--')

# displaying both graphs
plt.show()
