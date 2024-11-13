# Python3 code to demonstrate
# Remove Rear K characters from String List
# using map() + lambda

# initializing list
test_list = ['Manjeets', 'Akashs', 'Akshats', 'Nikhils']

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 4

# using map() + lambda
# Remove Rear K characters from String List
res = list(map(lambda i: i[ : (len(i) - K)], test_list))

# printing result
print("The list after removing last characters : " + str(res))
