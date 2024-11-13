# Python3 code to demonstrate
# to get most frequent element
# using max() + set()

# initializing list
test_list = [9, 4, 5, 4, 4, 5, 9, 5, 4]

# printing original list
print("Original list : " + str(test_list))

# using max() + set() to
# get most frequent element
res = max(set(test_list), key=test_list.count)

# printing result
print("Most frequent number is : " + str(res))
