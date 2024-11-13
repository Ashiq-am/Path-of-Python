# Python3 code to demonstrate working of
# Chunk Tuples to N
# using list comprehension

# initialize tuple
test_tup = (10, 4, 5, 6, 7, 6, 8, 3, 4)

# printing original tuple
print("The original tuple : " + str(test_tup))

# initialize N
N = 3

# Chunk Tuples to N
# using list comprehension
res = [test_tup[i : i + N] for i in range(0, len(test_tup), N)]

# printing result
print("The tuples after chunking are : " + str(res))
