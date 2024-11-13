# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values1 = [20, 35, 30, 25, 40]
values2 = [15, 25, 20, 30, 35]
groups = ['Group 1', 'Group 2', 'Group 1', 'Group 2', 'Group 1']

# Create a DataFrame from the data
data = pd.DataFrame({'categories': categories, 'values1': values1,
					'values2': values2, 'groups': groups})

# Convert values to radians
data['angle1'] = np.deg2rad(data['values1'])
data['angle2'] = np.deg2rad(data['values2'])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot the first group of bars
sns.barplot(x='categories', y='angle1', hue='groups', data=data,
			ax=ax, palette='Set1')

# Plot the second group of bars, offsetting them slightly to avoid overlap
sns.barplot(x='categories', y='angle2', hue='groups', data=data, ax=ax,
			palette='Set2', alpha=0.7)

# Set the radial axis label
ax.set_rticks([])

# Add a title
ax.set_title('Grouped Circular Bar Plot', pad=20)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, title='Groups', loc='upper right', bbox_to_anchor=(1.3, 1))

# Display the plot
plt.show()
