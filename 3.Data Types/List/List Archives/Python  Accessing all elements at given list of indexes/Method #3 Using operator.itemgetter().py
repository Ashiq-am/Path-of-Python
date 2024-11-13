# Python3 code to demonstrate
# to get elements from indices
# using operator.itemgetter()
from operator import itemgetter

# initializing lists
test_list = [9, 4, 5, 8, 10, 14]
index_list = [1, 3, 4]

# printing original lists
print("Original list : " + str(test_list))
print("Original index list : " + str(index_list))

# using operator.itemgetter() to
# elements from list
res_list = list(itemgetter(*index_list)(test_list))

# printing result
print("Resultant list : " + str(res_list))
