# import library
import numpy as np

# create a 1d-array
a = np.array(("geeks", "for ",
			"geeks"))

# create a 1d-array
b = np.array(("my", "name",
			"sachin"))

# convert 1d-arrays into
# columns of 2d-array
c = np.column_stack((a, b))

print(c)
