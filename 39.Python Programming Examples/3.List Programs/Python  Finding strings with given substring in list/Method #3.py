# Python code to demonstrate
# to find strings with substrings
# using re + search()
import re

# initializing list
test_list = ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']

# printing original list
print ("The original list is : " + str(test_list))

# initializing substring
subs = 'Geek'

# using re + search()
# to get string with substring
res = [x for x in test_list if re.search(subs, x)]

# printing result
print ("All strings with given substring are : " + str(res))
