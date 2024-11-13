# Python3 code to demonstrate
# moving element to end
# using append() + pop() + index()

# initializing list
test_list = ['3', '5', '7', '9', '11']

# printing original list
print ("The original list is : " + str(test_list))

# using append() + pop() + index()
# moving element to end
test_list.append(test_list.pop(test_list.index(5)))

# printing result
print ("The modified element moved list is : " + str(test_list))
