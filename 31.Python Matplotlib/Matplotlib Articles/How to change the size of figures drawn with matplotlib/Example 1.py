# We start by importing matplotlib
import matplotlib.pyplot as plt

# Plotting a figure of width 6 and height 3
plt_1 = plt.figure(figsize=(6, 3))

# Let's plot the equation y=2*x
x = [1, 2, 3, 4, 5]

# y = [2,4,6,8,10]
y = [x*2 for x in x]

# plt.plot() specifies the arguements for x-axis
# and y-axis to be plotted
plt.plot(x, y)

# To show this figure object, we use the line,
# fig.show()
plt.show()
