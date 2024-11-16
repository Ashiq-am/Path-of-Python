# importing library numpy as np
import numpy as np

# creating array as first_name
first_name = np.array(['Geeks'],
					dtype = np.str)
print("Printing first name array:")
print(first_name)

# creating array as last name
last_name = np.array(['forGeeks'],
					dtype = np.str)
print("Printing last name array:")
print(last_name)

# concate first_name and last_name
# into new array named as full_name
full_name = np.char.add(first_name, last_name)
print("\nPrinting concatenate array as full name:")
print(full_name)
