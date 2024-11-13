# Python3 code to demonstrate working of
# Index Power List
# Using pow() + list comprehension + enumerate()
from math import pow

# initializing list
test_list = [6, 9, 1, 8, 4, 7]

# printing original list
print("The original list is : " + str(test_list))

# pow() does task of getting power
# list comprehension for 1 liner alternative
res = [int(pow(ele, idx)) for idx, ele in enumerate(test_list)]

# printing result
print("Powered elements : " + str(res))
