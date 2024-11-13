# Python3 code to demonstrate working of
# Remove Units from Value List
# Using replace() + strip() + list comprehension
import re

# initializing list
test_list = ["54 kg", "23 kg", "12kg", "19 kg"]

# printing original list
print("The original list is : " + str(test_list))

# initializing unit
unit = "kg"

# Remove Units from Value List
# Using replace() + strip() + list comprehension
res = [sub.replace(unit, "").strip() for sub in test_list]

# printing result
print("List after unit removal : " + str(res))
