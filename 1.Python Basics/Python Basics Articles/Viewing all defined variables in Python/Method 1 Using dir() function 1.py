# Create a new variable and store all
# built-in functions within it using dir( ).
not_my_data = set(dir())

# Define some variables of various types.
var2 = "Welcome to geeksforgeeks"
var3 = {"1": "a", "2": "b"}
var4 = 25
var5 = [1, 2, 3, 4, 5]
var6 = (58, 59)

# Again call dir and store it in a list
# subtracting the built-in variables stored
# previously.
my_data = set(dir()) - not_my_data

# Iterate over the whole list is stored.
for name in my_data:

    # Exclude the un-necessary variable named not_my_data
    if name != "not_my_data":
        val = eval(name)
        print(name, "is", type(val), "and is equal to ", val)
