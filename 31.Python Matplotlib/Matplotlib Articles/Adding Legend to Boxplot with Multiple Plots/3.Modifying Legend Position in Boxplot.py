box = ax.boxplot(data, patch_artist=True)

# Set labels for x-axis
ax.set_xticklabels(['Dataset 1', 'Dataset 2', 'Dataset 3'])

# Define colors for each dataset
colors = ['lightblue', 'lightgreen', 'lightcoral']

# Apply colors to each boxplot
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Create custom labels
labels = ['Dataset 1', 'Dataset 2', 'Dataset 3']

# Add a legend
# Positioning the legend
ax.legend([box['boxes'][i] for i in range(len(colors))], labels, loc='upper left')


# Show the plot
plt.title('Boxplot with Legend for Multiple Datasets')
plt.show()
