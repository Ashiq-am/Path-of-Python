# Python3 code to demonstrate working of
# Concatenate Random characters in String List
# Using loop + choice()
import random

# initializing list
test_list = ["Gfg", "is", "Best", "for", "Geeks"]

# printing original list
print("The original list is : " + str(test_list))

res = ''
for ele in test_list:
    # Concatenating random elements
    res += random.choice(ele)

# printing results
print("Concatenated String : " + str(res))
