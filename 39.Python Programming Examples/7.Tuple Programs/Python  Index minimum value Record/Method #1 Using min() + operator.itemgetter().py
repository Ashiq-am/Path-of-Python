# Python 3 code to demonstrate
# Index minimum value Record
# using min() + itemgetter()
from operator import itemgetter

# initializing list
test_list = [('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]

# printing original list
print ("Original list : " + str(test_list))

# using min() + itemgetter()
# Index minimum value Record
res = min(test_list, key = itemgetter(1))[0]

# printing result
print ("The name with minimum score is : " + res)
