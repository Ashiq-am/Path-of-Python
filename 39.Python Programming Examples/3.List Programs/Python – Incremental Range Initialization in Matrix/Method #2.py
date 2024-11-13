# Python3 code to demonstrate
# Incremental Range Initialization in Matrix
# using list comprehension

# Initializing row
r = 4

# Initializing col
c = 3

# Initializing range
rang = 5

# Incremental Range Initialization in Matrix
# using list comprehension
res = [[rang * c * y + rang * x for x in range(c)] for y in range(r)]

# printing result
print ("Matrix after Initialization : " + str(res))
