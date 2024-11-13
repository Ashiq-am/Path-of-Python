# Python3 code to demonstrate working of
# Split Numeric String into K digit integers
# Using int() + slice + loop

# initializing string
test_str = '457336842'

# printing original string
print("The original string is : " + str(test_str))

# initializing substring
K = 3

res = []
for idx in range(0, len(test_str), K):
    # converting to int, after slicing
    res.append(int(test_str[idx: idx + K]))

# printing result
print("Converted number list : " + str(res))
