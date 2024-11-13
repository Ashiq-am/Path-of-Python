import matplotlib.pyplot as plt


x =[1, 2, 3, 4, 5]
y =[2, 4, 6, 8, 10]

plt.plot(x, y)

# Increasing head_width of
# the arrow by setting
# head_width parameter
plt.arrow(2, 4, 2, 2,
		head_width = 0.2,
		width = 0.05)

plt.show()
