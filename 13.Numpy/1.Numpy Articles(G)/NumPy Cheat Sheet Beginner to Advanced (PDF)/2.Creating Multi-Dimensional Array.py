# create a NumPy array from a list
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = [9, 10, 11, 12]
print(np.array([list_1, list_2, list_3]))

# create a NumPy array using numpy.empty()
print(np.empty([4, 3], dtype=int))
