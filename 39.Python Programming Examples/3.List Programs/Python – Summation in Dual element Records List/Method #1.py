# Python3 code to demonstrate
# Summation in Dual element Records List
# using list comprehension

# Initializing list
test_list = [(6, 7), (2, 4), (8, 9), (6, 2)]

# printing original lists
print("The original list is : " + str(test_list))

# Summation in Dual element Records List
# using list comprehension
res = [ele[0] + ele[1] for ele in test_list]

# printing result
print ("Summation pairs in tuple list : " + str(res))
