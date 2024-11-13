# Define colors
colors = ['blue' if i != max_index else 'red' for i in range(len(df))]

# Create a barplot with custom colors
sns.barplot(x='Category', y='Values', data=df, palette=colors)
plt.show()
