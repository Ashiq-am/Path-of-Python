# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(16)
y = np.sin(x / 3)

fig, ax = plt.subplots()

ax.step(x, y + 2, color ='green')
ax.plot(x, y + 2, 'o--', color ='black', alpha = 0.3)

def show_figure(fig):

	dummy = plt.figure()
	new_manager = dummy.canvas.manager
	new_manager.canvas.figure = fig
	fig.set_canvas(new_manager.canvas)

show_figure(fig)

fig.suptitle("""matplotlib.figure.Figure.set_canvas() 
function Example\n\n""", fontweight ="bold")

plt.show()
