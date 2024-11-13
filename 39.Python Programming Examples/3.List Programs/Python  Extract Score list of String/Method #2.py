# Python3 code to demonstrate working of
# Extract Score list of String
# using list comprehension + zip() + ascii_lowercase + dict()
import string

# initialize list and string
test_list = [3, 4, 5, 7, 5, 8, 1, 5, 7, 10,
             6, 7, 9, 11, 3, 1, 3, 6, 7, 9,
             7, 4, 6, 4, 2, 1]

test_str = "geeksforgeeks"

# printing original list and string
print("The original list : " + str(test_list))
print("The original string : " + str(test_str))

# Extract Score list of String
# using list comprehension + zip() + ascii_lowercase + dict()
temp = dict(zip(string.ascii_lowercase, test_list))
res = [temp[ele] for ele in test_str]

# printing result
print("The Score list is : " + str(res))
