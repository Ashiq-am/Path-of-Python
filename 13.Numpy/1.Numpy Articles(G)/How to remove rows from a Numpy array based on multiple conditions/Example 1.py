nparray = np.delete(nparray, np.where(
	(nparray >= 5) & (nparray <= 20))[0], axis=0)

print("After deletion of rows containing numbers between 5 and 20: \n", nparray)
