# Create a scatter plot with empty circles
plt.figure(figsize=(8, 6))

# s is the size of the circles
plt.scatter(x, y, facecolors='none', edgecolors='blue', s=100)
plt.title('Scatter Plot with Empty Circles')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.grid(True)
plt.show()
