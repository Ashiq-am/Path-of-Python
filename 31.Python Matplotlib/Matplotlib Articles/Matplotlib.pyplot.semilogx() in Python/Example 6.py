# import required library
import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows = 1,
						ncols = 2,
						figsize = (15,9))
# Or equivalently, "plt.tight_layout()"
fig.tight_layout()


# subplot 1
x1 = [-1, 2, 0,
	-3, 5, 9,
	10, -3, -8,
	15, 12, 0.1,0.9]

y1 = [5, -2, 0,
	10, 20, 30,
	25, 28, 16,
	25, 28, 3, 5]

plt.subplot(1,2,1)

# plotting the graph
plt.semilogx(x1, y1,
			marker = ".",
			markersize = 20,
			nonposx = "clip",
			color = "green" )

# set the y-axis label
plt.ylabel('---y---')

# set the x-axis label
plt.xlabel('---x---')

# set the title
plt.title('CLIP')

# plot with grid
plt.grid(True)


# subplot 2
x2 = [-1, 2, 0,
	-3, 5, 9,
	10, -3, -8,
	15, 12, 0.1, 0.9]

y2 = [5, -2, 0,
	10, 20, 30,
	25, 28, 16,
	25, 28, 3, 5]

plt.subplot(1,2,2)
plt.semilogx(x2, y2,
			nonposx = "mask",
			color ="green",
			linewidth = 4,
			marker = ".",
			markersize = 20)

# set the title
plt.title('MASK')

# set the y-axis label
plt.ylabel('---y---')

# set the x-axis label
plt.xlabel('---x---')

# plot with grid
plt.grid(True)

# show the plot
plt.show()
