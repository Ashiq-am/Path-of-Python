# Python3 code to demonstrate
# Remove front K elements in String List
# using map() + lambda

# initializing list
test_list = ['Manjeet', 'Akash', 'Akshat', 'Nikhil']

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 3

# using map() + lambda
# Remove front K elements in String List
res = list(map(lambda i: i[K :], test_list))

# printing result
print("The list after removing initial K characters : " + str(res))
