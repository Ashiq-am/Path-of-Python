# Create a boxplot that automatically ignores NaN values
plt.boxplot(data)
plt.title('Boxplot Automatically Ignoring NaNs')
plt.ylabel('Values')
plt.xticks([1, 2, 3], ['Group 1', 'Group 2', 'Group 3'])
plt.show()
