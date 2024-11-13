# Implementation of matplotlib function
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.text(3, 4, 'GeeksforGeeks', style ='italic',
		fontsize = 30, color ="green")

ax.set(xlim =(0, 8), ylim =(0, 8))
ax.set_title('matplotlib.axes.Axes.text() Example',
			fontsize = 14, fontweight ='bold')

plt.show()
