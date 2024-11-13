# Python3 code to demonstrate working of
# Dual Tuple Alternate summation
# Using list comprehension + sum()

# initializing list
test_list = [(4, 1), (5, 6), (3, 5), (7, 5), (1, 10)]

# printing original list
print("The original list is : " + str(test_list))

# summation using sum(), list comprehension offers shorthand
res = sum([test_list[idx][0] if idx % 2 == 0 else test_list[idx][1] for idx in range(len(test_list))])

# printing result
print("Summation of Alternate elements of tuples : " + str(res))
