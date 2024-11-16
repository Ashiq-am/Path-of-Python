# Creating another array with 100 random values
array2 = [np.random.randint(100) for i in range(100)]
std = np.std(array2)
mean = np.mean(array2)
AlreadySelected = []
# Creating outliers on the upper end
i = 0
while (i < 5):
    x = np.random.choice(array2)  # Randomly selecting a value from the array
    y = x + mean * 4
    array2 = np.append(array2, y)
    if (x not in AlreadySelected):
        AlreadySelected.append(y)

        i += 1

    else:
        continue

plt.boxplot(array2)
plt.title('Array with outliers')
plt.show()
