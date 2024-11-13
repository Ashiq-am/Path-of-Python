# Python3 code to demonstrate
# K Character Split String
# using list comprehension + split()

# initializing string
test_string = "GfG_is_Best"

# printing original string
print("The original string : " + str(test_string))

# initializing K
K = '_'

# using list comprehension + split()
# K Character Split String
res = [i for j in test_string.split(K) for i in (j, K)][:-1]

# print result
print("The list without omitting Character : " + str(res))
