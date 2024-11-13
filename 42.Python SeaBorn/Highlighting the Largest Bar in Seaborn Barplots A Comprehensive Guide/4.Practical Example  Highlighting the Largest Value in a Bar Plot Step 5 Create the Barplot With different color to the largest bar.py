# Create a barplot with custom colors
sns.barplot(x='Category', y='Values', data=df, palette=colors)
plt.title('Bar Plot Highlighting the Largest Value')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()
