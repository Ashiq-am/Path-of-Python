# Python3 code to demonstrate working of
# Consecutive element swapping in String
# using join() + zip() + generator expression

# initializing string
test_str = "gfgisbesty"

# printing original string
print("The original string is : " + test_str)

# Consecutive element swapping in String
# using join() + zip() + generator expression
res = ''.join([char[1] + char[0] for char in zip(test_str[::2], test_str[1::2])])

# printing result
print("String after Consecutive Swapping : " + str(res))
