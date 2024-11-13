ax = sns.heatmap(df, annot=False, cmap='viridis')
annotate_diagonal(df.values, mask, ax, color='white')

# Add titles and labels
plt.title('Heatmap with Diagonal Annotations')
plt.xlabel('Columns')
plt.ylabel('Rows')
plt.show()
