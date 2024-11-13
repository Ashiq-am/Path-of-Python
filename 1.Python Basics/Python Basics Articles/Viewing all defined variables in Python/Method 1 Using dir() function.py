# Define some variables of various types
# that are not starting with '__'
var2 = "Welcome to geeksforgeeks"
var3 = {"1": "a", "2": "b"}
var4 = 25
var5 = [1, 2, 3, 4, 5]
var6 = (58, 59)

# call dir and store it in a variable.
# It stores all the variable names defined
# before in the form of a list
# and stores the variable names as a string.
all_variables = dir()

# Iterate over the whole list where dir( )
# is stored.
for name in all_variables:

    # Print the item if it doesn't start with '__'
    if not name.startswith('__'):
        myvalue = eval(name)
        print(name, "is", type(myvalue), "and is equal to ", myvalue)
