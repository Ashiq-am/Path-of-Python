# Create a boxplot with varying box widths
plt.boxplot(data, widths=[0.3, 0.5, 0.7])  # Different widths for each box
plt.title('Boxplot with Varying Widths')
plt.ylabel('Values')
plt.xticks([1, 2, 3], ['Group 1', 'Group 2', 'Group 3'])
plt.show()
