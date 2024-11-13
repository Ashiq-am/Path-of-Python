# Python3 code to demonstrate
# to get random number from list
# using random.randrange
import random

# initializing list
test_list = [1, 4, 5, 2, 7]

# printing original list
print ("Original list is : " + str(test_list))

# using random.randrange() to
# get a random number
rand_idx = random.randrange(len(test_list))
random_num = test_list[rand_idx]

# printing random number
print ("Random selected number is : " + str(random_num))
