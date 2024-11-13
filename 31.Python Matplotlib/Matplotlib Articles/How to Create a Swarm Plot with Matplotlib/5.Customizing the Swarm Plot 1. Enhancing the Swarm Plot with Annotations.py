# Add annotations to the plot
plt.scatter(df['Jittered_Category'], df['Value'], s=50, alpha=0.6)
plt.xticks(ticks=range(len(categories)), labels=categories)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Swarm Plot with Annotations')

# Highlight a point
highlight = df.iloc[10]
plt.annotate('Highlighted Point', (highlight['Jittered_Category'], highlight['Value']),
             xytext=(10, 20), textcoords='offset points', arrowprops=dict(arrowstyle='->'))

plt.show()
