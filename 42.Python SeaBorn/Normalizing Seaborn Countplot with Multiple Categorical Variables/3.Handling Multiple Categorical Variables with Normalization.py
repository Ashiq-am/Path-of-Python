# Group by 'day', 'sex', and 'time'
grouped_data = tips.groupby(['day', 'sex', 'time']).size().reset_index(name='counts')

# Calculate total counts for each combination of 'day' and 'time'
grouped_data['total'] = grouped_data.groupby(['day', 'time'])['counts'].transform('sum')

# Calculate proportion
grouped_data['proportion'] = grouped_data['counts'] / grouped_data['total']

# Plot the normalized countplot
sns.barplot(x="day", y="proportion", hue="sex", data=grouped_data, ci=None)
plt.ylabel('Proportion')
plt.title('Normalized Countplot by Day, Sex, and Time')
plt.show()
