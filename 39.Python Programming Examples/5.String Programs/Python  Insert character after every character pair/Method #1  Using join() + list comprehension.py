# Python3 code to demonstrate working of
# Insert character after every character pair
# Using join() + list comprehension

# initializing string
test_str = "GeeksforGeeks"

# printing original string
print("The original string is : " + test_str)

# Using join() + list comprehension
# Insert character after every character pair
res = ', '.join(test_str[i:i + 2] for i in range(0, len(test_str), 2))

# printing result
print("The string after inserting comma after every character pair : " + res)
