# Python3 code to demonstrate working of
# Insert character after every character pair
# Using zip() + join()

# initializing string
test_str = "GeeksforGeeks"

# printing original string
print("The original string is : " + test_str)

# Using zip() + join()
# Insert character after every character pair
res = ', '.join(a + b for a, b in zip(test_str[::2], test_str[1::2]))

# printing result
print("The string after inserting comma after every character pair : " + res)
