# Python3 code to demonstrate working of
# Convert String to N chunks tuple
# Using list comprehension + tuple()

# initialize string
test_string = "ggggffffgggg"

# printing original string
print("The original string : " + str(test_string))

# initialize N
N = 4

# Convert String to N chunks tuple
# Using list comprehension + tuple()
res = tuple(test_string[ i : i + N] for i in range(0, len(test_string), N))

# printing result
print("Chunked String into tuple : " + str(res))
