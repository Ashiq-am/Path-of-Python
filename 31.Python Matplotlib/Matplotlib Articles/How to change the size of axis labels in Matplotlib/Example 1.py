import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [9, 8, 7, 6, 5]

fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(x, y)

ax.set_xlabel('x-axis', fontsize = 12)
ax.set_ylabel('y-axis', fontsize = 10)

plt.show()
