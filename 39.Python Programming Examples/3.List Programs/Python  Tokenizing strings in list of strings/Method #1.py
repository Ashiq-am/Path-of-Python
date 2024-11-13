# Python3 code to demonstrate
# Tokenizing strings in list of strings
# using list comprehension + split()

# initializing list
test_list = ['Geeks for Geeks', 'is', 'best computer science portal']

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + split()
# Tokenizing strings in list of strings
res = [sub.split() for sub in test_list]

# print result
print("The list after split of strings is : " + str(res))
