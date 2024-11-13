# Python3 code to demonstrate
# Remove Rear K characters from String List
# using list comprehension + list slicing

# initializing list
test_list = ['Manjeets', 'Akashs', 'Akshats', 'Nikhils']

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 4

# using list comprehension + list slicing
# Remove Rear K characters from String List
res = [sub[ : len(sub) - K] for sub in test_list]

# printing result
print("The list after removing last characters : " + str(res))
