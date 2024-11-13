# Python3 code to demonstrate working of
# Join Tuples to Integers in Tuple List
# Using map() + join() + int()

# initializing list
test_list = [(4, 5), (5, 6), (1, 3), (6, 9)]

# printing original list
print("The original list is : " + str(test_list))

# Join Tuples to Integers in Tuple List
# Using map() + join() + int()
res = [int(''.join(map(str, idx))) for idx in test_list]

# printing result
print("The joined result : " + str(res))
