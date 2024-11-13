# plotting histograms
plt.hist(data['petal_length'],
		label='petal_length')

plt.hist(data['sepal_length'],
		label='sepal_length')

plt.legend(loc='upper right')
plt.title('Overlapping')
plt.show()
