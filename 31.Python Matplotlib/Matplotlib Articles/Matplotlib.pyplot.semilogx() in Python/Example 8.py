# import required library
import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows = 2,
						ncols = 2,
						figsize = (10,7))

# Or equivalently, "plt.tight_layout()"
fig.tight_layout()

# subplot 1
plt.subplot(2, 2, 1)
x = [1, 11]
y = [4, 6]

# plot the graph
plt.semilogx(x, y, marker = ".",
			markersize = 20,
			color = "green")

# set the title
plt.title("Without subsx - line ")

# plot with grid
plt.grid(True)


# subplot 2
plt.subplot(2, 2, 2)
x = [1, 11]
y = [4, 6]

# plot the graph
plt.semilogx(x, y, subsx = [2, 3, 9, 10],
			marker = ".", markersize = 20,
			color = "green")

# set the title
plt.title("With subsx - line ")
plt.grid(True)


# subplot 3
plt.subplot(2, 2, 3)
x = [1, 11]
y = [4, 6]
plt.semilogx(x, y, 'g^', marker = ".",
			markersize = 20,
			color = "blue")
plt.title("Without subsx - symbol ")
plt.grid(True)


# subplot 4
plt.subplot(2, 2, 4)
x = [1, 11]
y = [4, 6]
plt.semilogx(x, y, 'g^', subsx=[2, 3, 9, 10],
			marker = ".", markersize = 20,
			color = "blue")
plt.title("With subsx - symbol ")
plt.grid(True)

plt.show()
