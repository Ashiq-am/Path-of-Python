import seaborn as sns
import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values_1 = [10, 15, 20, 25, 30]
y_values_2 = [5, 10, 15, 20, 25]

plt.plot(x_values, y_values_1, label='Group 1')
plt.plot(x_values, y_values_2, label='Group 2')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.title('GFG Line')
plt.legend()
plt.grid(True)
plt.show()
