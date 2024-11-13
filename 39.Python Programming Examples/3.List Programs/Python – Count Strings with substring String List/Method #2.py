# Python code to demonstrate
# Count Strings with substring String List
# using filter() + lambda + len()

# initializing list
test_list = ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']

# printing original list
print ("The original list is : " + str(test_list))

# initializing substring
subs = 'Geek'

# using filter() + lambda + len()
# Count Strings with substring String List
res = len(list(filter(lambda x: subs in x, test_list)))

# printing result
print ("All strings count with given substring are : " + str(res))
