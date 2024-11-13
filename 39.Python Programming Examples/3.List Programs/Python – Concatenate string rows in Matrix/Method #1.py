# Python3 code to demonstrate
# Row String Concatenation Matrix
# using join() + list comprehension

# initializing list
test_list = [['gfg', ' is', ' best'], ['Computer', ' Science'], ['GeeksforGeeks']]

# printing original list
print("The original list : " + str(test_list))

# using join() + list comprehension
# Row String Concatenation Matrix
res = [''.join(idx for idx in sub) for sub in test_list ]

# print result
print("The row concatenation in matrix : " + str(res))
