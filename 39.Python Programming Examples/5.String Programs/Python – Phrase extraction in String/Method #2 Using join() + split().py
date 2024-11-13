# Python3 code to demonstrate working of
# Phrase extraction in String
# Using join() + split()

# initializing string
test_str = 'Geeksforgeeks is best for geeks and CS'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 2

# Phrase extraction in String
# Using join() + split()
res = ' '.join(test_str.split()[K:-(K - 1)])

# printing result
print("String after phrase removal : " + str(res))
