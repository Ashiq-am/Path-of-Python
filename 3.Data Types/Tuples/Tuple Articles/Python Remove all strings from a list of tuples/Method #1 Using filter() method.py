# Python code to remove all strings from a list of tuples

# Check function to check isinstance
def check(x):
    return not isinstance(x, str)


# creating list of tuples
listOfTuples = [('string', 'Paras'), (2, 'Jain'), (3, 'GFG'),
                (4, 'Cyware'), (5, 'Noida')]

# using filter
output = ([tuple(filter(check, x)) for x in listOfTuples])

# printing output
print(output)
