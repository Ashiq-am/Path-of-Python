# Python3 code to demonstrate working of
# Slice String from Tuple ranges
# using loop + list slicing

# initialize list and string
test_list = [(2, 4), (5, 9), (13, 17), (24, 27)]

test_str = "geeksforgeeks is best for geeks and programming"

# printing original list and string
print("The original list : " + str(test_list))
print("The original string : " + str(test_str))

# Slice String from Tuple ranges
# using loop + list slicing
for front, rear in reversed(test_list):
    test_str = test_str[: front] + test_str[rear + 1:]

# printing result
print("The String after slicing is : " + str(test_str))
