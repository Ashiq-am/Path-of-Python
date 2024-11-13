# Python3 code to demonstrate working of
# Concatenate Random characters in String List
# Using list comprehension + choice() + join()
import random

# initializing list
test_list = ["Gfg", "is", "Best", "for", "Geeks"]

# printing original list
print("The original list is : " + str(test_list))

# characters joining using join()
res = ''.join([random.choice(ele) for ele in test_list])

# printing results
print("Concatenated String : " + str(res))
