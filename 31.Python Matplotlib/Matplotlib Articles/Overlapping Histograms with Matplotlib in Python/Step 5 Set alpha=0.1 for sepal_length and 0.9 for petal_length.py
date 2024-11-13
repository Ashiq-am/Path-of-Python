plt.hist(data['petal_length'],
		alpha=0.9,
		label='petal_length')

plt.hist(data['sepal_length'],
		alpha=0.1,
		label='sepal_length')

plt.legend(loc='upper right')
plt.title('Overlapping with alpha=0.1 and 0.9 for sepal and petal')
plt.show()
