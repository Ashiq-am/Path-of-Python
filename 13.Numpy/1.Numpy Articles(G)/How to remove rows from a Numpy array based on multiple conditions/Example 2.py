nparray = np.delete(nparray, np.where(
	(nparray[:, 0] >= 25) & (nparray[:, 0] <= 35))[0], axis=0)

print("After deletion of rows whose first element is between 25 and 35:\n", nparray)
