# Create a scatter plot with empty circles
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='X', y='Y', edgecolor='blue', facecolor='none', s=100)
plt.title('Scatter Plot with Empty Circles using Seaborn')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.grid(True)
plt.show()
