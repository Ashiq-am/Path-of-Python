# Remove NaN values from the dataset
cleaned_data = [np.array(group)[~np.isnan(group)] for group in data]

# Create a boxplot with cleaned data
plt.boxplot(cleaned_data)
plt.title('Boxplot After Removing NaNs')
plt.ylabel('Values')
plt.xticks([1, 2, 3], ['Group 1', 'Group 2', 'Group 3'])
plt.show()
