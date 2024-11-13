import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [9, 8, 7, 6, 5]

fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(x, y)

plt.xticks(fontsize = 15)
plt.show()
