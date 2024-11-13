# Python3 code to demonstrate working of
# Convert Delimiter seperated list to Number
# Using join() + split() + int()

# initializing string
test_str = "1@6@7@8@5@8@9"

# printing original string
print("The original string is : " + str(test_str))

# initializing Delimiter
delim = "@"

# join used over splitted result
# final result casted using int()
res = int("".join(test_str.split(delim)))

# printing result
print("Constructed integer : " + str(res))
