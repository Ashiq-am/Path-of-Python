# Customizing markers and colors
sns.scatterplot(data=combined_data, x='x', y='y', hue='label', style='label', palette=['blue', 'red'], markers=['o', 's'])

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Customized Scatter Plot of Two Datasets')
plt.legend(title='Dataset')

# Display the plot
plt.show()
