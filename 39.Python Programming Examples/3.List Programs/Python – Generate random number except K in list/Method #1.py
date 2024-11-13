# Python3 code to demonstrate
# Generate random number except K in list
# using choice() + list comprehension
import random

# Initializing list
test_list = [4, 7, 8, 4, 6, 10]

# printing original list
print("The original list is : " + str(test_list))

# Initializing K
K = 4

# Generate random number except K in list
# using choice() + list comprehension
res = random.choice([ele for ele in test_list if ele != K])

# printing result
print ("The random number except K is : " + str(res))
