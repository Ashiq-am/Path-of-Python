# importing the matplotlib library
import matplotlib.pyplot as plt

# values on x-axis
x = [1, 2, 3, 4, 5]
# values on y-axis
y = [1, 2, 3, 4, 5]

# naming the x and y axis
plt.xlabel('x - axis')
plt.ylabel('y - axis')

# plotting a line plot with it's default size
print("Plot in it's default size: ")
plt.plot(x, y)
plt.show()

# plotting a line plot after changing it's width and height
f = plt.figure()
f.set_figwidth(4)
f.set_figheight(1)

print("Plot after re-sizing: ")
plt.plot(x, y)
plt.show()
