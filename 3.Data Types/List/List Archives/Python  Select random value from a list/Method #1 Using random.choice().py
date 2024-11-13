# Python3 code to demonstrate
# to get random number from list
# using random.choice()
import random

# initializing list
test_list = [1, 4, 5, 2, 7]

# printing original list
print ("Original list is : " + str(test_list))

# using random.choice() to
# get a random number
random_num = random.choice(test_list)

# printing random number
print ("Random selected number is : " + str(random_num))
