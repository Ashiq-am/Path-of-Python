# Python3 code to demonstrate
# use of dict() and zip() built-ins to demonstrate
# initializing dictionary with list

keys = range(4)
new_dict = dict(zip(keys, ([] for _ in keys)))

print(new_dict)  # performing append
# shows no error
new_dict[0].append('GeeksforGeeks')

# printing result
print("New dictionary created : " + str(dict(new_dict)))
