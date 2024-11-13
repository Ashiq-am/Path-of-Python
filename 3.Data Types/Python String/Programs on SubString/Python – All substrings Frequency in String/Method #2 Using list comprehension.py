# Python3 code to demonstrate working of
# All substrings Frequency in String
# Using list comprehension

# initializing string
test_str = "abababa"

# printing original string
print("The original string is : " + str(test_str))

# list comprehension to extract substrings and frequency
res = dict()
for ele in [test_str[idx: j] for idx in range(len(test_str)) for j in range(idx + 1, len(test_str) + 1)]:
    res[ele] = 1 if ele not in res.keys() else res[ele] + 1

# printing result
print("Extracted frequency dictionary : " + str(res))
