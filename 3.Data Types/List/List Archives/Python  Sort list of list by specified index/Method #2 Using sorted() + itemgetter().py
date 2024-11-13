# Python3 code to demonstrate
# to sort list of list by given index
# using sorted() + itemgetter()
from operator import itemgetter

# initializing list
test_list = [['Rash', 4, 28], ['Varsha', 2, 20], ['Nikhil', 1, 20], ['Akshat', 3, 21]]

# printing original list
print ("The original list is : " + str(test_list))

# using sort() + lambda
# to sort list of list
# sort by second index
res = sorted(test_list, key = itemgetter(1))

# printing result
print ("List after sorting by 2nd element of lists : " + str(res))
