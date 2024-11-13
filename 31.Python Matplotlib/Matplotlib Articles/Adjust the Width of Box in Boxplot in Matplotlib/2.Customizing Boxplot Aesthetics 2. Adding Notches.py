plt.boxplot(data, widths=0.5, notch=True)  # Add notches
plt.title('Boxplot with Notches')
plt.ylabel('Values')
plt.xticks([1, 2, 3], ['Group 1', 'Group 2', 'Group 3'])
plt.show()
