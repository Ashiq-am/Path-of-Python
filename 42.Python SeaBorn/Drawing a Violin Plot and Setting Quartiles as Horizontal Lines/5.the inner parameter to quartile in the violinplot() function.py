# Create the base violin plot
plt.figure(figsize=(8, 6))
sns.violinplot(x='Category', y='Values', data=data, inner=None)

# Loop through each category to add quartile lines
for i, category in enumerate(data['Category'].unique()):
    q1, q2, q3 = quartiles[category]

    # Plot horizontal lines for each quartile
    plt.hlines(y=q1, xmin=i - 0.2, xmax=i + 0.2, color='red', linestyle='--', label='25th Percentile' if i == 0 else "")
    plt.hlines(y=q2, xmin=i - 0.2, xmax=i + 0.2, color='green', linestyle='-',
               label='50th Percentile (Median)' if i == 0 else "")
    plt.hlines(y=q3, xmin=i - 0.2, xmax=i + 0.2, color='blue', linestyle='--',
               label='75th Percentile' if i == 0 else "")

# Add title and legend
plt.title('Violin Plot with Custom Quartiles as Horizontal Lines')
plt.legend()
plt.show()
