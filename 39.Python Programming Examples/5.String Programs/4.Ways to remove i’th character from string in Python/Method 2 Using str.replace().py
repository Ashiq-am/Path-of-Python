# Python code to demonstrate
# method to remove i'th character
# using replace()

# Initializing String
test_str = "GeeksForGeeks"

# Printing original string
print ("The original string is : " + test_str)

# Removing char at pos 3
# using replace
new_str = test_str.replace('e', '')

# Printing string after removal
# removes all occurrences of 'e'
print ("The string after removal of i'th character( doesn't work) : " + new_str)

# Removing 1st occurrence of s, i.e 5th pos.
# if we wish to remove it.
new_str = test_str.replace('s', '', 1)

# Printing string after removal
# removes first occurrences of s
print ("The string after removal of i'th character(works) : " + new_str)
