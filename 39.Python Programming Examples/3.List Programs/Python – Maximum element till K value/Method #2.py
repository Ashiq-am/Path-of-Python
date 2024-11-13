# Python 3 code to demonstrate
# Maximum element till K value
# using list comprehension

# initializing list
test_list = [1, 7, 5, 6, 3, 8]

# initializing k
k = 4

# printing list
print ("The list : " + str(test_list))

# using list comprehension
# Maximum element till K value
res = max([i for i in test_list if i <= k])

# printing the intersection
print ("The maximum number till K : " + str(res))
