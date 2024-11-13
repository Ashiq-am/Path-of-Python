# Python3 code to demonstrate working of
# Count of Words with specific letter
# Using filter() + lambda + len() + split()

# initializing string
test_str = 'geeksforgeeks is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing letter
letter = "e"

# extracting desired count using len()
# filter() used to check for letter existence
res = len(list(filter(lambda ele : letter in ele, test_str.split())))

# printing result
print("Words count : " + str(res))
