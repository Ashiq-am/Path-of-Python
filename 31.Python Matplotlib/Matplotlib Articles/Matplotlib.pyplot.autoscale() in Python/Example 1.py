# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = [1,2,3]

# corresponding y axis values
y = [2,4,1]

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')

# naming the y axis
plt.ylabel('y - axis')

plt.autoscale()
plt.show()
