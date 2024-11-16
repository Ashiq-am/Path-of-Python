# importing library
import numpy as np

# creating dictionary as key as
# a number and value as its cube
dict_created = {0: 0, 1: 1, 2: 8, 3: 27,
				4: 64, 5: 125, 6: 216}

# printing type of dictionary created
print(type(dict_created))

# converting dictionary to
# numpy array
res_array = np.array(list(dict_created.items()))

# printing the converted array
print(res_array)

# printing type of converted array
print(type(res_array))
