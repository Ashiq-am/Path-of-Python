# Creating the scatter plot
sns.scatterplot(data=combined_data, x='x', y='y', hue='label')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot of Two Datasets')
plt.legend(title='Dataset')

# Display the plot
plt.show()
