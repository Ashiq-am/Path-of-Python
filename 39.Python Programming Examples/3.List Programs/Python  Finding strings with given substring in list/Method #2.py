# Python code to demonstrate
# to find strings with substrings
# using filter() + lambda

# initializing list
test_list = ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']

# printing original list
print ("The original list is : " + str(test_list))

# initializing substring
subs = 'Geek'

# using filter() + lambda
# to get string with substring
res = list(filter(lambda x: subs in x, test_list))

# printing result
print ("All strings with given substring are : " + str(res))
