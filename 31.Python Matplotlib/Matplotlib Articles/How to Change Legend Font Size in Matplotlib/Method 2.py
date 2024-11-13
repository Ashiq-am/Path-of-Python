import matplotlib.pyplot as plt

plt.figure(figsize = (8 , 5))

plt.plot([1, 2, 4, 8, 30, 1])
plt.plot([1, 6, 13, 20, 38, 1])
plt.plot([1, 4, 8, 14, 20, 1])
plt.plot([1, 3, 4, 5, 10, 1])

#Using prop keyword in legend to change font size
plt.legend(['blue', 'orange', 'green', 'red'],
		prop = {'size' : 20},
		loc = 'upper left', shadow = True,
		facecolor = 'yellow')

plt.show()
