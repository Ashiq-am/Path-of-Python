# Python 3 code to demonstrate
# Index Value Summation List
# using list comprehension

# initializing list
test_list = [1, 4, 5, 6, 7]

# Printing list
print ("The original list is : " + str(test_list))

# using list comprehension to
# Index Value Summation List
res = [sum(list((i, test_list[i]))) for i in range(len(test_list))]

print ("The list index-value summation is : " + str(res))
