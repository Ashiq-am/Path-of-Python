# import required module
import matplotlib.pyplot as plt

# first data point
x = [1, 2, 3, 4]
y = [4, 1, 3, 6]

# depict first scatted plot
plt.scatter(x, y, c='green')

# second data point
x = [5, 6, 7, 8]
y = [1, 3, 5, 2]

# depict second scatted plot
plt.scatter(x, y, c='red')

# depict illustrattion
plt.show()
