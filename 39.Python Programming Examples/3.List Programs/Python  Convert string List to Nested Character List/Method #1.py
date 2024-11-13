# Python3 code to demonstrate working of
# Convert String List to Nested Character List
# using split() + list comprehension

# initialize list
test_list = ["a, b, c", "gfg, is, best", "1, 2, 3"]

# printing original list
print("The original list : " + str(test_list))

# Convert String List to Nested Character List
# using split() + list comprehension
res = [char.split(', ') for char in test_list]

# printing result
print("List after performing conversion : " + str(res))
