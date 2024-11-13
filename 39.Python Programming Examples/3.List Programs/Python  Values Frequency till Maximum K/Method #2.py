# Python 3 code to demonstrate
# Values Frequency till Maximum K
# using sum()

# initializing list
test_list = [1, 7, 5, 6, 3, 8]

# initializing k
k = 4

# printing list
print ("The list : " + str(test_list))

# using sum()
# to get numbers < k
count = sum(i < k for i in test_list)

# printing the result
print ("The numbers smaller than 4 : " + str(count))
