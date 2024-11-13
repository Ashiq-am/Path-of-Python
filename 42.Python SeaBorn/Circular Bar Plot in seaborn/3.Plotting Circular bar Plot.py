# Convert values to radians
data['angle'] = np.deg2rad(data['values'])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Plot the bars
sns.barplot(x='categories', y='angle', hue='categories',
			data=data, ax=ax, palette='viridis', legend=False)

# Set the radial axis label
ax.set_rticks([])

# Display the plot
plt.show()
