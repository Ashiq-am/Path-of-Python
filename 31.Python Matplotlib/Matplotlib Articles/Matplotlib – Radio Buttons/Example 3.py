import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons

# plotting between the interval -π and π
x = np.linspace(-np.pi, np.pi)

# trignometric functions to plot
p = 2*np.sin(x)
q = np.sin(x)
r = np.cos(x)
s = 2*np.cos(x)
fig, ax = plt.subplots()

l, = ax.plot(x, p, lw=3, color='red')
plt.subplots_adjust(left=0.3)

rax = plt.axes([0.05, 0.7, 0.15, 0.2])
radio = RadioButtons(rax, ('2sin(x)',
						'sin(x)',
						'cos(x)',
						'2cos(x)'))

# function performed on clicking the radio buttons
def sinefunc(label):
	sindict = {'2sin(x)': p,
			'sin(x)': q,
			'cos(x)': r,
			'2cos(x)': s}
	data = sindict[label]
	l.set_ydata(data)
	plt.draw()


radio.on_clicked(sinefunc)

# plot grid
ax.grid()

# x and y-coordinates for graph creation
x = np.linspace(0, 2*np.pi, 200)
y = np.cos(x**2)

# sub-plot for radio button with
# left, bottom, width, height values
rax2 = plt.axes([0.05, 0.15, 0.15, 0.2])
radio_button = RadioButtons(rax2, ('red',
								'blue',
								'green'))

# function performed on switching radiobuttons
def colorfunc(label2):
	l.set_color(label2)
	plt.draw()


radio_button.on_clicked(colorfunc)

plt.show()
