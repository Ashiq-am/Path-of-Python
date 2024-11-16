arr1 = np.array([[2, 4], [6, 8]])
arr2 = np.array([[3, 5], [7, 9]])

# combining on axis 0
gfg = np.concatenate((arr1, arr2), axis = 0)
print(gfg)

# combining on axis 1
gfg = np.concatenate((arr1, arr2), axis = 1)
print("\n", gfg)

# combining on axis None
gfg = np.concatenate((arr1, arr2), axis = None)
print("\n", gfg)

# stacking two arrays on one another
print(np.stack((arr1, arr2), axis=1))
