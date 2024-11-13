# Python implementation of converting
# a string into a dictionary

# initialising first string
str1 = "Jan, Feb, March"
str2 = "January | February | March"

# splitting first string
# in order to get keys
keys = str1.split(", ")

# splitting second string
# in order to get values
values = str2.split("|")

# declaring the dictionary
dictionary = {}

# Merging all keys and values
# to generate items for
# the dictionary
dictionary = dict(zip(keys, values))

# printing the generated dictionary
print(dictionary)
