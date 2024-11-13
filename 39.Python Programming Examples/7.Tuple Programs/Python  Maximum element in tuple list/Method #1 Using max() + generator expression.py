# Python3 code to demonstrate working of
# Maximum element in tuple list
# using max() + generator expression

# initialize list
test_list = [(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]

# printing original list
print("The original list : " + str(test_list))

# Maximum element in tuple list
# using max() + generator expression
res = max(int(j) for i in test_list for j in i)

# printing result
print("The Maximum element of list is : " + str(res))
