# Python3 code to demonstrate working of
# Index Mapping Cypher
# Using loop + join()

# initializing string
test_str = "geeksforgeeks"

# printing original string
print("The original string is : " + test_str)

# initializing cypher string
cyp_str = "53410"

# Index Mapping Cypher
# Using loop + join()
res = [test_str[int(idx)] for idx in cyp_str]
res = ''.join(res)

# printing result
print("The deciphered value string : " + str(res))
