# Implementation of matplotlib function
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')

fig.text(0.3, 0.7,
		'GeeksforGeeks',
		style = 'italic',
		fontsize = 30,
		bbox ={'facecolor':'green',
				'alpha':0.6,
				'pad':10})

fig.text(0.35, 0.6,
		'Python matplotlib Module',
		fontsize = 15)

fig.text(0.35, 0.3,
		'Figure Class - Text Function')

fig.text(0, 0, 'by-Shubham Singh',
		verticalalignment ='bottom',
		horizontalalignment ='left',
		transform = ax.transAxes,
		color ='green',
		fontsize = 5)



ax.set(xlim =(0, 10), ylim =(0, 10))

fig.suptitle("""matplotlib.figure.Figure.text() 
function Example\n\n""", fontweight ="bold")

fig.show()
