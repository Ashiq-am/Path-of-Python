# the array is saved in the file geekfile.npy
np.save("geekfile", np.arange(5))

# the array is loaded into b
print(np.load("geekfile.npy"))
