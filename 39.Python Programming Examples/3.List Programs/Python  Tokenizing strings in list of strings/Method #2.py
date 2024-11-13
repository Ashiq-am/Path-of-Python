# Python3 code to demonstrate
# Tokenizing strings in list of strings
# using map() + split()

# initializing list
test_list = ['Geeks for Geeks', 'is', 'best computer science portal']

# printing original list
print("The original list : " + str(test_list))

# using map() + split()
# Tokenizing strings in list of strings
res = list(map(str.split, test_list))

# print result
print("The list after split of strings is : " + str(res))
