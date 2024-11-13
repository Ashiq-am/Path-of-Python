# Python3 code to demonstrate working of
# Remove random element from list
# Using randrange() + pop()
import random

# initializing list
test_list = [6, 4, 8, 9, 10]

# printing list
print("The original list : " + str(test_list))

# Remove random element from list
# Using randrange() + pop()
test_list.pop(random.randrange(len(test_list)))

# Printing result
print("List after removal of random number : " + str(test_list))
