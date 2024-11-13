import matplotlib.pyplot as plt


x =[1, 15, 27, 48, 50]
y =[1, 12, 22, 45, 67]

plt.plot(x, y)

# Setting alpha will make
# the rectangle transparent
plt.axvspan(10, 30, ymin = 0.15,
			ymax = 0.70, ec ='blue',
			color ='yellow',
			alpha = 0.5)

plt.show()
