# Python3 code to demonstrate working of
# Multilength String Split
# Using join() + list comprehension + next()

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing length list
cus_lens = [5, 3, 2, 3]

# join() performs characters to string conversion
# list comprehension provides shorthand to solve problem
stritr = iter(test_str)
res = ["".join(next(stritr) for idx in range(size)) for size in cus_lens]

# printing result
print("Strings after splitting : " + str(res))
