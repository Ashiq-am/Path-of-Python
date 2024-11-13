# Python3 code to demonstrate working of
# Sort String list by K character frequency
# Using sort() + count() + lambda

# initializing list
test_list = ["geekforgeeks", "is", "best", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 'e'

# "-" sign used to reverse sort
# inplace sort
test_list.sort(key = lambda ele: -ele.count(K))

# printing results
print("Sorted String : " + str(test_list))
