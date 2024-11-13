# Python3 code to demonstrate
# Minimum Sum of Consecutive Characters
# using zip() + min() + list comprehension

# initializing string
test_string = '6543452345456987653234'

# printing original string
print("The original string : " + str(test_string))

# using zip() + min() + list comprehension
# Minimum Sum of Consecutive Characters
test_string = list(test_string)
res = min(int(a) + int(b) for a, b in zip(test_string, test_string[1:]))

# print result
print("The minimum consecutive sum is : " + str(res))
