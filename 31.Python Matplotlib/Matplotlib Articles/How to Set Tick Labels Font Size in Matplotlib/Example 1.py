# importing libraries
import matplotlib.pyplot as plt

# creating data
x = list(range(1, 11, 1))
y = [s*s for s in x]

# ploting data
plt.plot(x, y)

# changing the fontsize of yticks
plt.yticks(fontsize=20)

# showing the plot
plt.show()
