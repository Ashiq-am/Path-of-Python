# Impute NaN values with the mean of each group
imputed_data = [np.nan_to_num(group, nan=np.nanmean(group)) for group in data]

# Create a boxplot with imputed data
plt.boxplot(imputed_data)
plt.title('Boxplot After Imputing NaNs with Mean')
plt.ylabel('Values')
plt.xticks([1, 2, 3], ['Group 1', 'Group 2', 'Group 3'])
plt.show()
