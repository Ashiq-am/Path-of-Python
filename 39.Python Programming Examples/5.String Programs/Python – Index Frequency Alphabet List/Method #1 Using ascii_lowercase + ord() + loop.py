# Python3 code to demonstrate working of
# Index Frequency Alphabet List
# Using ascii_lowercase + ord() + loop
from string import ascii_lowercase

# extracting start index
strt_idx = ord('a') - 1

res = []
for ele in ascii_lowercase:
    # multiplying Frequency
    res.append(ele * (ord(ele) - strt_idx))

# printing result
print("The constructed list : " + str(res))
