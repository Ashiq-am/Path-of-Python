# Python3 code to demonstrate working of
# Tuple list elements count
# using len() + generator expression

# initialize list
test_list = [(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]

# printing original list
print("The original list : " + str(test_list))

# Tuple list elements count
# using len() + generator expression
temp = list((int(j) for i in test_list for j in i))
res = len(temp)

# printing result
print("The tuple list elements count : " + str(res))
