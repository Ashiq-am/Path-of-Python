# Python3 code to demonstrate
# Alternate front - rear Sum
# using list comprehension

# initializing list
test_list = [1, 4, 5, 3, 6, 7]

# printing original list
print ("The original list is : " + str(test_list))

# Alternate front - rear Sum
# using list comprehension
res = [test_list[i] + test_list[len(test_list) - (i + 1)] for i in range(len(test_list) // 2)]

# printing result
print ("The alterate front - rear Sum list is : " + str(res))
