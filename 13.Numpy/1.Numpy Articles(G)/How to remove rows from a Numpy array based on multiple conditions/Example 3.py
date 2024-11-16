nparray = np.delete(nparray, np.where((nparray[:, 2] % 2 == 0) | (nparray[:, 4] % 3 == 0) | (nparray[:, 3] % 3 == 0))[0], axis=0)

print("After removng required rows :\n", nparray)
