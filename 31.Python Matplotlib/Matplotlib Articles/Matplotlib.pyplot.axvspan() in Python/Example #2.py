import matplotlib.pyplot as plt


x =[1, 15, 27, 48, 50]
y =[1, 12, 22, 45, 67]

plt.plot(x, y)

# Drawing rectangle starting
# x = 5 and extending till x = 15
# With vertical span starting at
# 25 % the length of y-axis
# And extending till the 80 % of
# axis And also we are setting
# the color of rectangle to yellow
# and its edge color to blue
plt.axvspan(5, 15, ymin = 0.25,
			ymax = 0.80, ec ='blue',
			color ='yellow')

plt.show()
