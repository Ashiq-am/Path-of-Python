import numpy as np


arr = np.array([4, 5, 8, 5, 6, 4,
				9, 2, 4, 3, 6])

# measures of dispersion
min = np.amin(arr)
max = np.amax(arr)
range = np.ptp(arr)
varience = np.var(arr)
sd = np.std(arr)

print("Array =", arr)
print("Measures of Dispersion")
print("Minimum =", min)
print("Maximum =", max)
print("Range =", range)
print("Varience =", varience)
print("Standard Deviation =", sd)
