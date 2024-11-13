# Python3 code to demonstrate
# List extension by K
# using list comprehension

# initializing list
test_list = [4, 5, 2, 8]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 3

# using list comprehension
# to extend list
res = [i for i in test_list for j in range(K)]

# printing result
print("The resultant list after extension is : " + str(res))
