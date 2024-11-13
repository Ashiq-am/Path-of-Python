# Python3 code to demonstrate
# Every Kth index Maximum in List
# using list comprehension + enumerate() + max()

# initializing list
test_list = [1, 4, 5, 6, 7, 8, 9, 12]

# printing the original list
print ("The original list is : " + str(test_list))

# initializing K
K = 3

# using list comprehension + enumerate() + max()
# Every Kth index Maximum in List
# max of every 3rd element
res = max([i for j, i in enumerate(test_list) if j % K == 0 ])

# printing result
print ("The max of every kth element : " + str(res))
