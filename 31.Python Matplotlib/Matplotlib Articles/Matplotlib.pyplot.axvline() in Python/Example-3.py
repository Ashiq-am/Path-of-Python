import matplotlib.pyplot as plt

x =[0, 5, 10, 15, 20]
y =[1, 3, 5, 6, 9]

plt.plot(x, y)

# Drawing vertical line from 25 %
# of the y-axis length to 75 %
# And also changing the linestyle
plt.axvline(x = 2.5, ymin = 0.25, ymax = 0.75,
			linewidth = 4, linestyle ="--",
			color ='red')

plt.show()
