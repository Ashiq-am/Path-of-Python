# Python3 code to demonstrate working of
# Get Top N elements from Records
# Using sorted() + itemgetter()
from operator import itemgetter

# Initializing list
test_list = [('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)]

# Initializing N
N = 2

# printing original list
print("The original list is : " + str(test_list))

# Get Top N elements from Records
# Using sorted() + itemgetter()
res = sorted(test_list, key = itemgetter(1), reverse = True)[:N]

# printing result
print("The top N records are : " + str(res))
