# Python3 code to demonstrate working of
# Number of repeated substrings in consecution
# Using split() + count() + list comprehension

# initializing string
test_str = 'geeksgeeks are geeksgeeksgeeks for all geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = "geeks"

# count() counts repetition
res = [sub.count(K) for sub in test_str.split(' ') if sub.count(K) != 0]

# printing result
print("String repetitions : " + str(res))
