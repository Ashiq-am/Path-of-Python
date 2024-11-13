# Python3 code to demonstrate
# repeat element K times
# using list comprehension

# initializing list of lists
test_list = [4, 5, 6]

# printing original list
print("The original list : " + str(test_list))

# declaring magnitude of repetition
K = 3

# using list comprehension
# repeat elements K times
res = [ele for ele in test_list for i in range(K)]

# printing result
print("The list after adding elements : " + str(res))
