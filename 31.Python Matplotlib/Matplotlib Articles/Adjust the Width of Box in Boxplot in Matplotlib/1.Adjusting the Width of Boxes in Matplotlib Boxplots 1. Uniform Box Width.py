# Create a boxplot with uniform box width
plt.boxplot(data, widths=0.5)  # Adjust the width here
plt.title('Boxplot with Adjusted Width')
plt.ylabel('Values')
plt.xticks([1, 2, 3], ['Group 1', 'Group 2', 'Group 3'])
plt.show()
