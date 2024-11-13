# Python3 code to demonstrate working of
# Remove Units from Value List
# Using list comprehesion + regex()
import re

# initializing list
test_list = ["54 kg", "23 kg", "12kg", "19 kg"]

# printing original list
print("The original list is : " + str(test_list))

# initializing unit
unit = "kg"

# Remove Units from Value List
# Using list comprehesion + regex()
res = re.findall('\d+', ' '.join(test_list))

# printing result
print("List after unit removal : " + str(res))
