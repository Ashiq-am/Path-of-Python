ax = sns.heatmap(df, annot=False, cmap='viridis')
# Annotate only the diagonal elements
annotate_diagonal(df.values, mask, ax)

plt.show()
