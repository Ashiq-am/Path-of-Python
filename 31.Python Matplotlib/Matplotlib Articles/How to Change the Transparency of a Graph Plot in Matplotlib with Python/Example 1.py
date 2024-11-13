# importing module
import matplotlib.pyplot as plt

# assigning x and y coordinates
y = [0, 1, 2, 3, 4, 5]
x = [0, 5, 10, 15, 20, 25]

# depicting the visualization
plt.plot(x, y, color='green', alpha=0.25)
plt.xlabel('x')
plt.ylabel('y')

# displaying the title
plt.title("Linear graph")

plt.show()
