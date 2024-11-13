# Python3 code to demonstrate working of
# Convert String list to Joined Single element
# Using join() + list comprehension

# initializing list
test_list = ['gfg', 'is', 'best']

# printing original list
print("The original list is : " + str(test_list))

# initializing delim
delim = "-"

# Convert String list to Joined Single element
# Using join() + list comprehension
res = [delim.join(test_list)]

# printing result
print("String after performing join : " + str(res))
