# Python3 code to demonstrate
# Double List
# using list comprehension

# Initializing list
test_list = [12, 67, 98, 34, 43]

# printing original list
print("The original list is : " + str(test_list))

# Double List
# using list comprehension
res = [ele + ele for ele in test_list]

# printing result
print("Double List is : " + str(res))
