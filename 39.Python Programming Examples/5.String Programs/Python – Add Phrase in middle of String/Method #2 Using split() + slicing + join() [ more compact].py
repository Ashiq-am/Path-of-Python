# Python3 code to demonstrate working of
# Add Phrase in middle of String
# Using split() + slicing + join()

# initializing string
test_str = 'geekforgeeks is for geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing mid string
mid_str = "best"

# splitting string to list
temp = test_str.split()
mid_pos = len(temp) // 2

# joining and construction using single line
res = ' '.join(temp[:mid_pos] + [mid_str] + temp[mid_pos:])

# printing result
print("Formulated String : " + str(res))
