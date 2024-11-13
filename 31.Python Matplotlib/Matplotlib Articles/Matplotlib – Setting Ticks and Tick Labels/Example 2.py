# import required module
import matplotlib.pyplot as plt

# assign coordinates
x = y = [i for i in range(0, 10)]
ax = plt.axes()

# depict illustration
plt.plot(x, y, color="lime")

# setting ticks for x-axis
ax.set_xticks([2, 4, 6, 8, 10])

# setting label for x tick
ax.set_xticklabels(['Geeks', 'for', 'geeks', '!'])

# setting ticks for y-axis
ax.set_yticks([1, 3, 5, 7, 9])

# setting label for y tick
ax.set_yticklabels(['A', 'B', 'C', 'D'])

plt.show()
