# Convert values to radians
data['angle'] = np.deg2rad(data['values'])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Plot the bars
bars = sns.barplot(x='categories', y='angle', hue='categories', data=data,
				ax=ax, palette='viridis', edgecolor='none', alpha=0.8, linewidth=0)

# Set the radial axis label
ax.set_rticks([])

# Add text labels to the bars
for bar, value in zip(bars.patches, data['values']):
	ax.text(bar.get_x() + bar.get_width() / 2,
			bar.get_height() + 0.1,
			str(value),
			ha='center', va='bottom', color='black', fontsize=10)

# Add category labels
ax.set_xticks(np.linspace(0, 2*np.pi, len(categories), endpoint=False))
ax.set_xticklabels(categories)

# Add a title
plt.title('Circular Bar Plot', pad=20)

# Display the plot
plt.show()
