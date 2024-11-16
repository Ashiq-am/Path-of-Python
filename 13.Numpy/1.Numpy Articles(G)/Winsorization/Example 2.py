# Creating an array with 100 random values
array = [np.random.randint(100) for i in range(100)]

# Creating outliers
# Here, the values which are selected for creating outliers
# are appended so that same outliers are not created again.
AlreadySelected = []
i = 0

# Creating 5 outliers on the lower end
while (i < 5):
	x = np.random.choice(array) # Randomly selecting a value from the array
	y = x - mean*3
	array = np.append(array, y)
	if (x not in already_selected):
		AlreadySelected.append(y)

		i += 1

	else:
		continue

# Creating 5 outliers on the upper end
i = 0
while (i < 5):
	x = np.random.choice(array) # Randomly selecting a value from the array
	y = x + mean*4
	array = np.append(array, y)
	if (x not in already_selected):
		AlreadySelected.append(y)

		i += 1

	else:
		continue

std = np.std(array) # Storing the standard deviation of the array
mean = np.mean(array) # Storing the mean of the array

plt.boxplot(array)
plt.title('Array with Outliers')
plt.show()
