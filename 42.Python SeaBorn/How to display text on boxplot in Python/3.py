# depict box plot visualiation
plt.figure(figsize=(10, 6))
sns.boxplot(data['Width (in cm)'])
plt.text(75, 0.07, 'Outliers beyond beyond 75% value', fontsize=14)
plt.show()
