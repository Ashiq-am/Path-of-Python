# Python3 code to demonstrate
# Descending Sort String Numbers
# using sort() + key

# initializing list
test_list = [ '4', '6', '7', '2', '1']

# printing original list
print ("The original list is : " + str(test_list))

# using sort() + key
# Descending Sort String Numbers
test_list.sort(key = int, reverse = True)

# printing result
print ("The resultant reverse sorted list : " + str(test_list))
