plt.hist(data['petal_length'],
		alpha=0.5, # the transaparency parameter
		label='petal_length')

plt.hist(data['sepal_length'],
		alpha=0.5,
		label='sepal_length')

plt.legend(loc='upper right')
plt.title('Overlapping with both alpha=0.5')
plt.show()
