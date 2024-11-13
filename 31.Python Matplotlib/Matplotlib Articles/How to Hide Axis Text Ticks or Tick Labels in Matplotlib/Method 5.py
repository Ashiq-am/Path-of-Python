import matplotlib.pyplot as plt

x = [5, 8, 15, 20, 30]
y = [15, 10, 8, 20, 15]
plt.plot(x, y, color='g', linewidth=5)

plt.xticks(x, labels=" ")
plt.yticks(y, labels=" ")

plt.show()
