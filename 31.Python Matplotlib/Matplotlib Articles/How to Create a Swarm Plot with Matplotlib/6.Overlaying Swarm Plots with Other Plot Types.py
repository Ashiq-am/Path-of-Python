# Create a box plot
plt.boxplot([df[df['Category'] == cat]['Value'] for cat in categories], positions=range(len(categories)))

# Overlay the swarm plot
plt.scatter(df['Jittered_Category'], df['Value'], c=df['Color'], s=50, alpha=0.6)
plt.xticks(ticks=range(len(categories)), labels=categories)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Swarm Plot Overlayed on Box Plot')
plt.show()
