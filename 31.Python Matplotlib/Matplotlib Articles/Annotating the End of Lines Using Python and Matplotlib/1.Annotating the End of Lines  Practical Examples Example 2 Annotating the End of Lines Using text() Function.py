import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y)

# Annotate the end of the line
plt.text(x[-1], y[-1], f'({x[-1]}, {y[-1]})', fontsize=9, horizontalalignment='right')

plt.show()
