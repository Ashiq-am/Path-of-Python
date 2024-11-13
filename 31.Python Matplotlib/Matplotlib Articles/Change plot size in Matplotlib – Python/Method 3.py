# importing the matplotlib library
import matplotlib.pyplot as plt

# values on x-axis
x = [1, 2, 3, 4, 5]
# values on y-axis
y = [1, 2, 3, 4, 5]

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# plotting a line plot with it's default size
plt.plot(x, y)
plt.show()

# changing the rc parameters and plotting a line plot
plt.rcParams['figure.figsize'] = [2, 2]

plt.plot(x, y)
plt.show()

plt.scatter(x, y)
plt.show()
