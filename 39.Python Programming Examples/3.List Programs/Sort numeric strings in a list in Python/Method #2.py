# Python3 code to demonstrate
# numeric string sorting
# using sort() + key

# initializing list
test_list = [ '4', '6', '7', '2', '1']

# printing original list
print ("The original list is : " + str(test_list))

# using sort() + key
# numeric string sorting
test_list.sort(key = int)

# printing result
print ("The resultant sorted list : " + str(test_list))
