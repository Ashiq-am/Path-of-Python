# Python3 code to demonstrate
# remove last character from list of strings
# using list comprehension + list slicing

# initializing list
test_list = ['Manjeets', 'Akashs', 'Akshats', 'Nikhils']

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + list slicing
# remove last character from list of strings
res = [sub[ : -1] for sub in test_list]

# printing result
print("The list after removing last characters : " + str(res))
