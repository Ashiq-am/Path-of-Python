# Python3 code to demonstrate
# remove elements less than and equal K
# using list comprehension + count()

# initializing list
test_list = [1, 4, 3, 2, 3, 3, 2, 2, 2, 1]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 2

# using list comprehension + count()
# remove elements less than K
res = [ i for i in test_list if test_list.count(i) > K]

# print result
print("The list removing elements less than and equal K : " + str(res))
