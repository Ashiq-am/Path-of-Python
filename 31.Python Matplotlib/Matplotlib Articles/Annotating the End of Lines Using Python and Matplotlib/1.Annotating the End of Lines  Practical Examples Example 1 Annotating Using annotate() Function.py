import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 8, 6, 10, 15]

plt.plot(x, y)

# Annotate the end of the line
plt.annotate(f'End: {y[-1]}', (x[-1], y[-1]), textcoords="offset points", xytext=(-10,10), ha='center', arrowprops=dict(arrowstyle="->"))

plt.show()
