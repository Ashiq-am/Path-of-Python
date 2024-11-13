# Python3 code to demonstrate working of
# Slice String from Tuple ranges
# using join() + any() + generator expression

# initialize list and string
test_list = [(2, 4), (5, 9), (13, 17), (24, 27)]

test_str = "geeksforgeeks is best for geeks and programming"

# printing original list and string
print("The original list : " + str(test_list))
print("The original string : " + str(test_str))

# Slice String from Tuple ranges
# using join() + any() + generator expression
res = "".join(test_str[idx] for idx in range(len(test_str)) \
              if not any(front <= idx <= rear for front, rear in test_list))

# printing result
print("The String after slicing is : " + str(res))
