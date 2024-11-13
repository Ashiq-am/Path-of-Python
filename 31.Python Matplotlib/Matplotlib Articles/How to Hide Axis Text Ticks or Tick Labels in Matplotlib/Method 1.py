import matplotlib.pyplot as plt

x1 = [5, 8, 10]
y1 = [12, 16, 8]
x2 = [6, 9, 12]
y2 = [14, 10, 8]

plt.plot(x1, y1, 'g', linewidth=7)
plt.plot(x2, y2, 'b', linewidth=7)

plt.title('Disabling xticks and yticks', fontsize=20)

plt.xlabel('X axis', fontsize=15)
plt.ylabel('Y axis', fontsize=15)

# disabling xticks by Setting xticks to an empty list
plt.xticks([])

# disabling yticks by setting yticks to an empty list
plt.yticks([])

plt.show()
