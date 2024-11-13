# Python code to demonstrate
# method to remove i'th character
# using join() + list comprehension

# Initializing String
test_str = "GeeksForGeeks"

# Printing original string
print ("The original string is : " + test_str)

# Removing char at pos 3
# using join() + list comprehension
new_str = ''.join([test_str[i] for i in range(len(test_str)) if i != 2])

# Printing string after removal
# removes ele. at 3rd index
print ("The string after removal of i'th character : " + new_str)
