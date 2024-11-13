# Histogram and Density Plot
plt.figure(figsize=(7, 5))
sns.histplot(data['Sunspots'], kde=True)
plt.xlabel('Number of Sunspots')
plt.ylabel('Frequency')
plt.title('Histogram and Density Plot')
plt.grid(True)
plt.show()
