# Python3 code to demonstrate
# remove last character from list of strings
# using map() + lambda

# initializing list
test_list = ['Manjeets', 'Akashs', 'Akshats', 'Nikhils']

# printing original list
print("The original list : " + str(test_list))

# using map() + lambda
# remove last character from list of strings
res = list(map(lambda i: i[ : -1], test_list))

# printing result
print("The list after removing last characters : " + str(res))
