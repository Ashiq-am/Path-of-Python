# Python3 code to demonstrate
# moving element to end
# using sort() + key = (__eq__)

# initializing list
test_list = ['3', '5', '7', '9', '11']

# printing original list
print ("The original list is : " + str(test_list))

# using sort() + key = (__eq__)
# moving element to end
test_list.sort(key = '5'.__eq__)

# printing result
print ("The modified element moved list is : " + str(test_list))
