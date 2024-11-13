# Adding a KDE line
sns.histplot(data, bins=30, kde=True, stat='density', color='purple', alpha=0.6)
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Normalized Histogram with KDE')
plt.show()
