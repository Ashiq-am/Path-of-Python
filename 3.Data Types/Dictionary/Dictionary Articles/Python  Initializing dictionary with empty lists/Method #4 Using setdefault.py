# Python3 code to demonstrate
# to initialize dictionary with list
# using setdefault

# initializing dict with lists
new_dict = {}
[new_dict.setdefault(x, []) for x in range(4)]

# performing append
# shows no error
new_dict[0].append('GeeksforGeeks')

# printing result
print("New dictionary created : " + str(dict(new_dict)))
