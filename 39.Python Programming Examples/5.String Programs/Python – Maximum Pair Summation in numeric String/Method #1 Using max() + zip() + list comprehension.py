# Python3 code to demonstrate
# Maximum Pair Summation in String
# using zip() + max() + list comprehension

# initializing string
test_string = '6543452345456987653234'

# printing original string
print("The original string : " + str(test_string))

# using zip() + max() + list comprehension
# Maximum Pair Summation in String
test_string = list(test_string)
res = max(int(a) + int(b) for a, b in zip(test_string, test_string[1:]))

# print result
print("The maximum consecutive sum is : " + str(res))
