# Python3 code to demonstrate
# to get random number from list
# using random.randint()
import random

# initializing list
test_list = [1, 4, 5, 2, 7]

# printing original list
print ("Original list is : " + str(test_list))

# using random.randint() to
# get a random number
rand_idx = random.randint(0, len(test_list)-1)
random_num = test_list[rand_idx]

# printing random number
print ("Random selected number is : " + str(random_num))
