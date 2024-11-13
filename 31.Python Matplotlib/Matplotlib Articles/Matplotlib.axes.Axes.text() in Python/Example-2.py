# Implementation of matplotlib function
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')

ax.text(3, 8, 'GeeksforGeeks',
		style ='italic',
		fontsize = 30,
		bbox ={'facecolor':'green',
			'alpha':0.6, 'pad':20})

ax.text(3.5, 6, 'Python matplotlib Module',
		fontsize = 15)

ax.text(3.5, 3, 'Axes Class - Text Function')

ax.text(0, 0, 'by-Shubham Singh',
		verticalalignment ='bottom',
		horizontalalignment ='left',
		transform = ax.transAxes,
		color ='green', fontsize = 5)



ax.set(xlim =(0, 10), ylim =(0, 10))
ax.set_title('matplotlib.axes.Axes.text() Example',
			fontsize = 14, fontweight ='bold')
plt.show()
