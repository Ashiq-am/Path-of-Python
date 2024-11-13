import matplotlib.pyplot as plt
import numpy as np

x = ['Rani', 'Meena', 'Raju', 'Jhansi', 'Ram']
y = [5, 7, 9, 2, 6]

plt.bar(x,y)

plt.text(3, 7, 'Student Marks',
		fontsize = 18, color = 'g')

plt.xlabel('Students', fontsize = 15)
plt.ylabel('Marks', fontsize = 15)

plt.annotate('Highest scored', xy = (2.4, 8),
			fontsize = 16, xytext = (3, 9),
			arrowprops = dict(facecolor = 'red'),
			color = 'g')

plt.show()
