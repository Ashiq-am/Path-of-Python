# import required modules
import numpy as np

# initialising the array to be validated
address_list = np.array(["person_1@abc.com",
						"person_2@abc.ccc",
						"person_3@xyz.com"])

# Calling the endswith method
# start = 0 : starts from the begining of
# a stringend = -4 : Ends at 4 places before
# the string ending
validated_array = np.char.endswith(address_list,
								suffix ="abc",
								start=0, end=-4)

print(validated_array)
