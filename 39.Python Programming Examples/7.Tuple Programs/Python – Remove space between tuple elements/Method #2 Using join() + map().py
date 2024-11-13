# Python3 code to demonstrate working of
# Remove space between tuple elements
# Using join() + map()

# initializing tuples
test_tuple = (4, 5, 7, 6, 8)

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Remove space between tuple elements
# Using join() + map()
res = "(" + ", ".join(map(str, test_tuple)) + ")"

# printing result
print("The tuple after space removal : " + str(res))
