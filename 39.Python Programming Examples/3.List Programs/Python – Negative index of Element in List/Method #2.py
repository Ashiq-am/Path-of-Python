# Python3 code to demonstrate working of
# Negative index of Element
# Using ~ operator + list slicing + index()

# initializing list
test_list = [5, 7, 8, 2, 3, 5, 1]

# printing original list
print("The original list is : " + str(test_list))

# initializing Element
K = 3

# -1 operator to reverse list, index() used to get index
res = ~test_list[::-1].index(K)

# printing result
print("The required Negative index : " + str(res))
