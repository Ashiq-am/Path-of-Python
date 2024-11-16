# create a NumPy array from a list
li = [1, 2, 3, 4]
print(np.array(li))

# create a NumPy array from a tuple
tup = (5, 6, 7, 8)
print(np.array(tup))

# create a NumPy array using fromiter()
iterable = (a for a in range(8))
print(np.fromiter(iterable, float))
