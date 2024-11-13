# When a list object is passed as
# parameters for the dir() function

# A list, which conatains
# a few random values
geeks = ["geeksforgeeks", "gfg", "Computer Science",
					"Data Structures", "Algorithms" ]


# dir() will also list out common
# attributes of the dictionary
d = {} # empty dictionary

# dir() will return all the available
# list methods in current local scope
print(dir(geeks))


# Call dir() with the dictionary
# name "d" as parameter. Return all
# the available dict methods in the
# current local scope
print(dir(d))
