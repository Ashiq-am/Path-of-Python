# Change the first occurrence of a value greater than 10 in each row to 50
for i in range(array.shape[0]):
    row = array[i]
    mask = row > 10
    if np.any(mask):
        index = np.argmax(mask)  # Find the index of the first True value
        array[i, index] = 50

print("\nArray after changing the first occurrence of values greater than 10 in each row:\n", array)
