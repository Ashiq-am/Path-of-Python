plt.boxplot(data, widths=0.5, boxprops=dict(color='orange'))  # Change box color
plt.title('Boxplot with Custom Color')
plt.ylabel('Values')
plt.xticks([1, 2, 3], ['Group 1', 'Group 2', 'Group 3'])
plt.show()
