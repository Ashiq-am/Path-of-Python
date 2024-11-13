# Python3 code to demonstrate working of
# Random Matrix Element
# Using random.choice() [if row number given]
import random

# initializing list
test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]

# printing original list
print("The original list is : " + str(test_list))

# initializing Row number
r_no = [0, 1, 2]

# choice() for random number, from_iterables for flattening
res = random.choice(test_list[random.choice(r_no)])

# printing result
print("Random number from Matrix Row : " + str(res))
