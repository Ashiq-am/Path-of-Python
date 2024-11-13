# plotting more than 2 overlapping histograms
plt.hist(data['sepal_width'],
		alpha=0.5,
		label='sepal_width',
		color='red') # customized color parameter

plt.hist(data['petal_width'],
		alpha=0.5,
		label='petal_width',
		color='green')

plt.hist(data['petal_length'],
		alpha=0.5,
		label='petal_length',
		color='yellow')

plt.hist(data['sepal_length'],
		alpha=0.5,
		label='sepal_length',
		color='purple')

plt.legend(loc='upper right')
plt.show()
