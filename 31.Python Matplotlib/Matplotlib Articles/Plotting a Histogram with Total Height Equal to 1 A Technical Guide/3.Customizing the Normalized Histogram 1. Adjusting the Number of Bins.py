# Adjusting the number of bins
plt.hist(data, bins=50, density=True, alpha=0.6, color='r')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Normalized Histogram with 50 Bins')
plt.show()
