# Python3 code to demonstrate
# to perform custom list split
# using itertools.chain() + zip()
from itertools import chain

# initializing string
test_list = [1, 4, 5, 6, 7, 3, 5, 9, 2, 4]

# initializing split index list
split_list = [2, 5, 7]

# printing original list
print ("The original list is : " + str(test_list))

# printing original split index list
print ("The original split index list : " + str(split_list))

# using itertools.chain() + zip()
# to perform custom list split
temp = zip(chain([0], split_list), chain(split_list, [None]))
res = list(test_list[i : j] for i, j in temp)

# printing result
print ("The splitted lists are : " + str(res))
