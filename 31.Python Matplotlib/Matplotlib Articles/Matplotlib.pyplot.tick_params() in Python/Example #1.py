# importing libraries
import matplotlib.pyplot as plt

# values of x and y axes
x = [i for i in range(5, 55, 5)]
y = [1, 4, 3, 2, 7, 6, 9, 8, 10, 5]

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')

plt.show()
