plt.figure(figsize=(8, 6))
sns.violinplot(x='Category', y='Values', data=data, inner=None, palette='muted')

# Adding quartile lines again
for i, category in enumerate(data['Category'].unique()):
    q1, q2, q3 = quartiles[category]
    plt.hlines(y=q1, xmin=i-0.2, xmax=i+0.2, color='red', linestyle='--')
    plt.hlines(y=q2, xmin=i-0.2, xmax=i+0.2, color='green', linestyle='-')
    plt.hlines(y=q3, xmin=i-0.2, xmax=i+0.2, color='blue', linestyle='--')

# Title, labels, and legend
plt.title('Violin Plot with Custom Quartiles as Horizontal Lines', fontsize=14)
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()
