# subplots() function you can draw
# multiple plots in one figure
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 5))

# set limit for x and y axis
axes.set_ylim(-100, 500)
axes.set_xlim(0, 250)

# style for plotting line
plt.style.use("ggplot")

# create 5 list to get store element
# after every iteration
x1, y1, y2, y3, y4 = [], [], [], [], []
myvar = count(0, 3)

def animate(i):
	x1.append(next(myvar))
	y1.append((l1[i]))
	y2.append((l2[i]))
	y3.append((l3[i]))
	y4.append((l4[i]))

	axes.plot(x1, y1, color="red")
	axes.plot(x1, y2, color="gray")
	axes.plot(x1, y3, color="blue")
	axes.plot(x1, y4, color="green")


# set ani variable to call the
# function recursively
anim = FuncAnimation(fig, animate, interval=30)
