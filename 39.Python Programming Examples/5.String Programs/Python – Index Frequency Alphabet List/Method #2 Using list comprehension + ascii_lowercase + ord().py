# Python3 code to demonstrate working of
# Index Frequency Alphabet List
# Using list comprehension + ascii_lowercase + ord()
from string import ascii_lowercase

# extracting start index
strt_idx = ord('a') - 1

# list comprehension to solve as one liner
res = [ele * (ord(ele) - strt_idx) for ele in ascii_lowercase]

# printing result
print("The constructed list : " + str(res))
