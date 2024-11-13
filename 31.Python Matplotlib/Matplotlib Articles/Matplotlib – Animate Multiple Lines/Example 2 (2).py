# set line_animation variable to call
# the function recursively
line_animation = animation.FuncAnimation(
	fig, updateline, frames=100, fargs=(data, l, data2, k))

line_animation.save("lines.mp4", writer=Writer)
