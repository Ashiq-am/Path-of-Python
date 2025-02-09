import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4]
y1 = [10, 20, 25, 30]
y2 = [15, 25, 20, 35]
# Customizing first line with solid style and red color
plt.plot(x, y1, label='Dataset A', color='red', linestyle='-', linewidth=2)

# Customizing second line with dashed style and blue color
plt.plot(x, y2, label='Dataset B', color='blue', linestyle='--', marker='o', markersize=8)

# Adding title and labels
plt.title('Customized Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Adding legend
plt.legend()

# Show the plot
plt.show()