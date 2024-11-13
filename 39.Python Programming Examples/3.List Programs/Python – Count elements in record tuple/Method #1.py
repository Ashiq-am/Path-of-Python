# Python3 code to demonstrate working of
# Record elements count
# using len() + generator expression

# initialize list
test_list = [(2, 4), (6, 7), (5, 1), (6, 10), (8, 7)]

# printing original list
print("The original list : " + str(test_list))

# Record elements count
# using len() + generator expression
res = len(list((int(j) for i in test_list for j in i)))

# printing result
print("The total count of list is : " + str(res))
