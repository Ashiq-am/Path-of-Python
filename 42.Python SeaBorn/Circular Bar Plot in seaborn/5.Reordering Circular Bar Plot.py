# Create a DataFrame from the data
data = pd.DataFrame({'categories': categories, 'values': values})

# Define the desired order of categories
custom_order = ['B', 'C', 'A', 'E', 'D']

# Reorder the DataFrame based on the custom order
data['categories'] = pd.Categorical(data['categories'],
									categories=custom_order, ordered=True)
data = data.sort_values('categories')

# Convert values to radians
data['angle'] = np.deg2rad(data['values'])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Plot the bars
bars = sns.barplot(x='categories', y='angle', hue='categories',
				data=data, ax=ax, palette='viridis')

# Set the radial axis label
ax.set_rticks([])

# Add text labels to the bars
for bar, value in zip(bars.patches, data['values']):
	ax.text(bar.get_x() + bar.get_width() / 2,
			bar.get_height() + 0.1,
			str(value),
			ha='center', va='bottom')

# Add category labels
ax.set_xticks(np.linspace(0, 2*np.pi, len(custom_order),
						endpoint=False))
ax.set_xticklabels(custom_order)

# Add a title
ax.set_title('Circular Bar Plot', pad=20)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, title='Categories', loc='upper right',
		bbox_to_anchor=(1.3, 1))

# Display the plot
plt.show()
