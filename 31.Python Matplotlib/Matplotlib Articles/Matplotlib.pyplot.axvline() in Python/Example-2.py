import matplotlib.pyplot as plt

x =[0, 5, 10, 15, 20]
y =[1, 3, 5, 6, 9]

plt.plot(x, y)
# Drawing vertical line from 25 %
# of the y-axis length to 80 %
# And also increasing the linewidth
plt.axvline(x = 2.5, ymin = 0.25, ymax = 0.80,
			linewidth = 8, color ='green')

plt.show()
