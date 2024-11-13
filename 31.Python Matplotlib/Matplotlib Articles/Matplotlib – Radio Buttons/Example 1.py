# import required modules as numpy,
# matplotlib and radiobutton widget
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons

# x and y-coordinates for graph creation
x = np.linspace(0, 2*np.pi, 200)
y = np.cos(x**2)

# Creating subplot and adjusting subplot
fig, ax = plt.subplots()
l, = ax.plot(x, y, color='yellow')
plt.subplots_adjust(left=0.4)
ax.set_title('Plot with RadioButtons',
			fontsize=18)

# sub-plot for radio button with
# left, bottom, width, height values
rax = plt.axes([0.1, 0.15, 0.2, 0.2])
radio_button = RadioButtons(rax, ('yellow',
								'red',
								'blue',
								'green'))

# function performed on switching the
# radiobuttons
def colorfunc(label):
	l.set_color(label)
	plt.draw()


radio_button.on_clicked(colorfunc)

plt.show()
