# import required modules
import numpy as np

# initialising the array to be validated
address_list = np.array(["person_1@abc.com",
						"person_2@abc.ccc",
						"person_3@xyz.com"])

# Calling the endswith method
validated_array = np.char.endswith(address_list,
								suffix = ".com")

print(validated_array)
