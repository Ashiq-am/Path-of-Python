# Python3 code to demonstrate working of
# Group Similar items to Dictionary Values List
# Using dictionary comprehension + Counter()
from collections import Counter

# initializing list
test_list = [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]

# printing original list
print("The original list : " + str(test_list))

# using * operator to perform multiplication
res = {key : [key] * val for key, val in Counter(test_list).items()}

# printing result
print("Similar grouped dictionary : " + str(res))
