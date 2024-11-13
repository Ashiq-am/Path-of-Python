# Python3 code to demonstrate working of
# Non-Overlapping occurrences of N Repeated K character
# Using split() + sum

# initializing string
test_str = 'aaabaaaabbaa'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = "a"

# initializing N
N = 2

# getting split char
spl_char = [ele for ele in test_str if ele != K][0]

# getting split list
temp = test_str.split(spl_char)

# getting Non-Overlapping occurrences
res = sum( len(sub) // N for sub in temp)

# printing result
print("The Non-Overlapping occurrences : " + str(res))
