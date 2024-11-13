# Python3 code to demonstrate
# to get tuple info. of maximum value tuple
# using sorted() + lambda

# initializing list
test_list = [('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]

# printing original list
print ("Original list : " + str(test_list))

# using sorted() + lambda
# to get tuple info. of maximum value tuple
res = sorted(test_list, key = lambda i: i[1], reverse = True)[0][0]

# printing result
print ("The name with maximum score is : " + res)
