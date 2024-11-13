# Python3 code to demonstrate
# assign unique value to list elements
# using list comprehension + enumerate

# initializing list
test_list = [1, 4, 6, 1, 4, 5, 6]

# printing the original list
print ("The original list is : " + str(test_list))

# using list comprehension + enumerate
# assign unique value to list elements
temp = {i: j for j, i in enumerate(set(test_list))}
res = [temp[i] for i in test_list]

# printing result
print ("The unique value list is : " + str(res))
