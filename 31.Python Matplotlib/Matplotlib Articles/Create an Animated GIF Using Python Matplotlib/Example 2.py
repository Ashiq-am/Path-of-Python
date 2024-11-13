# funciton takes frame as an input
def AnimationFunction(frame):

	# setting y according to frame
	# number and + x. It's logic
	y = np.cos(x+2*np.pi*frame/100)

	# line is set with new values of x and y
	line_plotted.set_data((x, y))
