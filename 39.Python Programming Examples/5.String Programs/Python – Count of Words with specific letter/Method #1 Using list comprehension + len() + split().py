# Python3 code to demonstrate working of
# Count of Words with specific letter
# Using list comprehension + len() + split()

# initializing string
test_str = 'geeksforgeeks is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing letter
letter = "e"

# extracting desired count using len()
# list comprehension is used as shorthand
res = len([ele for ele in test_str.split() if letter in ele])

# printing result
print("Words count : " + str(res))
