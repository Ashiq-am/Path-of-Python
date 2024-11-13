# Implementation of matplotlib function
import matplotlib.pyplot as plt


def new_figure():

	fig = plt.figure()
	plt.plot([0, 1], [2, 3])
	plt.close(fig)
	return fig

def show_figure(fig):

	dummy = plt.figure()
	new_manager = dummy.canvas.manager
	new_manager.canvas.figure = fig
	fig.set_canvas(new_manager.canvas)

fig = new_figure()
show_figure(fig)

fig.suptitle("""matplotlib.figure.Figure.set_canvas() 
function Example\n\n""", fontweight ="bold")

plt.show()
