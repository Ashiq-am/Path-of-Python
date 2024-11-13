# Python3 code to demonstrate working of
# Uppercase Half String
# Using list comprehension + join() + upper()

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# computing half index
hlf_idx = len(test_str) // 2

# join() used to create result string
res = ''.join([test_str[idx].upper() if idx >= hlf_idx else test_str[idx]
               for idx in range(len(test_str))])

# printing result
print("The resultant string : " + str(res))
